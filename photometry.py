''' photometry.py:
Measures flux densities in files specified in files.py
using configuration settings in your local phot_config.py
(see example_config folder for a dummy config file).
It returns the frequencies, flux densities, errors and target information
and saves results and plots (if these options are set on in the phot_config.py file).
Source apertures can be set in the source.py file.

Example usage:
nu, flux, flux_err, source = photometry.photometry(custom_source=0, warnings_on=0, verbose=1)


Version 1.01 [Jan 2019]
Roke Cepeda-Arroita
Stuart Harper
roke.cepeda-arroita@manchester.ac.uk
stuart.harper@manchester.ac.uk
'''


# TODO: add functionality for variable custom_source in order to be able to dinamically change source properties
# For now, this setting does nothing.


def photometry(custom_source=0, warnings_on=0, verbose=1):

    # Import core modules

    import aperphot
    import numpy as np
    import healpy as hp


    # Import input configuration file

    from config_phot import targets, maps, saveAperdir, save_aper, save_hist, save_fluxes


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

        for i in range(len(APObj.unpix)):
    	    pix = np.arange(APObj.unpix[i])
    	    nside = int(np.sqrt(APObj.unpix[i]/12.))
    	    _lat, _lon = hp.pix2ang(nside, pix)
    	    _lon *= 180./np.pi
    	    _lat = (np.pi/2. - _lat)*180./np.pi
    	    lon += [_lon]
    	    lat += [_lat]


        # Get Flux from aperphot

        flux, err, nu = APObj.AperPhot(lon, lat, target)

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


    return APObj.nu, flux, err, target
