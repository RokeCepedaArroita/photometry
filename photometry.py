''' photometry.py:
Measures flux densities in files specified in files.py
using configuration settings in your local phot_config.py
(see example_config folder for a dummy config file).
It returns the frequencies, flux densities, errors and target information
and saves results and plots (if these options are set on in the phot_config.py file).
Source apertures can be set in the source.py file. In order to dynamically change the
source, pass a custom source in a structure like the examples in source.py when you
call the photometry code (i.e custom_source = your_custom_source).

Example usage:
nu, flux, flux_err, source = photometry.photometry(custom_source=None, warnings_on=False, verbose=True)


Version 2.0 [Dec 2024]
Roke Cepeda-Arroita
Stuart Harper
roke.cepeda-arroita@manchester.ac.uk
stuart.harper@manchester.ac.uk
'''


def photometry(custom_source=None, warnings_on=False, verbose=True, rescale_random_errors=None, throw_NaN=None):


    # Import core modules

    import aperphot
    import numpy as np
    import healpy as hp


    # Import input configuration file

    from config_phot import targets, maps, saveAperdir, save_aper, save_hist, save_fluxes, mode, effective_beam_area, scale_random_noise_by_beam_area
    from config_phot import throw_NaN as config_throw_NaN

    # Use function argument if provided, otherwise use config value

    throw_NaN = throw_NaN if throw_NaN is not None else config_throw_NaN


    # If we have a custom source then set its properties

    if not isinstance(custom_source, type(None)):
        targets = [custom_source]


    # Mute warnings

    if not warnings_on:
        import warnings
        warnings.filterwarnings("ignore")


    # Load Maps

    APObj = aperphot.aperphot(maps)



    # Loop Over Targets

    for target in targets:
        nside = int(np.sqrt(APObj.data[0].size/12.))
        lon = []
        lat = []

        # Check the 'low_s2n_treatment' flag and set 'scale_random_noise_by_beam_area'
        if 'low_s2n_treatment' in target:
            if target['low_s2n_treatment'] == 'Yes':
                scale_random_noise_by_beam_area = True
                print('\nUsing low signal to noise scaling for background noise\n')
        else:
            scale_random_noise_by_beam_area = False


        for i in range(len(APObj.unpix)):
    	    pix = np.arange(APObj.unpix[i])
    	    nside = int(np.sqrt(APObj.unpix[i]/12.))
    	    _lat, _lon = hp.pix2ang(nside, pix)
    	    _lon *= 180./np.pi
    	    _lat = (np.pi/2. - _lat)*180./np.pi
    	    lon += [_lon]
    	    lat += [_lat]

        # Calculate solid areas of primary and background apertures in steradians
        target['primary_sol_ang_sr'] = np.pi*target['ra'][0]*target['rb'][0]*(np.pi/180.)**2 # area of primary aperture in steradians
        target['background_sol_ang_sr'] = (np.pi*target['ira'][0]*target['irb'][0]-np.pi*target['ira'][0]*target['ifrac'][0]*target['irb'][0]*target['ifrac'][0]) *(np.pi/180.)**2 # area of backround aperture in steradians


        # Get Flux from aperphot
        flux, err, nu = APObj.AperPhot(lon, lat, target, mode=mode, throw_NaN=throw_NaN, scale_random_noise_by_beam_area=scale_random_noise_by_beam_area, effective_beam_area=effective_beam_area, rescale_random_errors=rescale_random_errors)

        if not isinstance(target['AUX'], type(None)):
            ancil = np.loadtxt(target['AUX'])
            APObj.nu = np.concatenate((APObj.nu, ancil[:,0]))
            flux = np.concatenate((flux, ancil[:,1]))
            err = np.concatenate((err, ancil[:,2]))


    # Pre-Photometry Info

    if verbose:

        # Calculate Values

        NFREQ = np.size(APObj.nu)
        NGOOD = np.size(flux[flux>0])
        NNEG = np.size(flux[flux<0])
        NZERO = np.size(flux[flux==0])
        NNAN = sum(np.isnan(flux))
        PRIMARYAREA = np.pi*target['ra'][0]*target['rb'][0] # area of primary aperture in squared degrees
        BACKAREA = np.pi*target['ira'][0]*target['irb'][0]-np.pi*target['ira'][0]*target['ifrac'][0]*target['irb'][0]*target['ifrac'][0] # area of secondary aperture in squared degrees

        print('\n*********************** SOURCE INFORMATION ***********************\n')
        print('SOURCE = {}, GALACTIC_COORDS = G{:+.2f}{:+.2f}'.format(target['name'], target['phi'][0], target['theta'][0]))
        print('PRIMARY = [RA = {:.1f}, RB = {:.1f}, PANG = {:.1f}, FRAC = {:.1f}, AR = {:.1f}]'.format(target['ra'][0],target['rb'][0],target['pang'][0],target['frac'][0],PRIMARYAREA))
        print('BCKGRND = [RA = {:.1f}, RB = {:.1f}, PANG = {:.1f}, FRAC = {:.1f}, AR = {:.1f}'.format(target['ira'][0],target['irb'][0],target['ipang'][0],target['ifrac'][0],BACKAREA))
        print('           BACK_GALACTIC_COORDS = G{:+.2f}{:+.2f}, SWEEP = {:.1f}]\n'.format(target['iphi'][0],target['itheta'][0],target['isweep'][0]))
        print('\n************** PHOTOMETRY INFORMATION *************\n')
        print('NFREQ = {}, NGOOD = {}, NEG = {}, ZERO = {}, NAN = {}'.format(NFREQ, NGOOD, NNEG, NZERO, NNAN))

        for nu, jansky, jansky_err, i in zip(nu, flux, err, np.arange(1,len(nu))):
            if i == 1:
                print('FREQ = {:.2E}   FLUX = {:.2E}   ERR = {:.2E}'.format(nu, jansky, jansky_err))
            else:
                print('       {:.2E}          {:.2E}         {:.2E}'.format(nu, jansky, jansky_err))


        print('\n')


    # Here add information to the source such as the primary aperture's solid angle, which is crucial for fitting!




    return APObj.nu, flux, err, target
