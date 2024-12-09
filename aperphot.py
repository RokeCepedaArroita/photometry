import numpy as np
import healpy as hp
import matplotlib.pyplot as plt
from config_phot import maps, saveAperdir, save_aper, save_hist, save_fluxes

d2r = np.pi/180.
r2d = 180./np.pi

from mpl_toolkits.mplot3d import Axes3D

def rotatelon(x, y, z, dlon):
    xr =  x*np.cos(dlon) + y*np.sin(dlon)
    yr = -x*np.sin(dlon) + y*np.cos(dlon)
    zr = z*1.
    return xr, yr, zr

def rotatelat(x, y, z, dlat):
    xr =  x*np.cos(dlat) + z*np.sin(dlat)
    yr =  y*1.
    zr = -x*np.sin(dlat) + z*np.cos(dlat)
    return xr, yr, zr


class aperphot():

    def __init__(self, maps):
        self.maps = maps

        # # Old code, read maps normally
        # self.data = [hp.read_map(m['name'],verbose=False) for m in maps]

        # Roke's addition: when reading the maps replace hp.UNSEEN with np.nan
        self.data = [self.replace_unseen(hp.read_map(m['name'])) for m in maps]

        self.npixs = [m.size for m in self.data]
        self.unpix = np.unique(self.npixs)
        self.nu = np.array([m['frequency'] for m in maps])
        self.calerr = np.array([m['CALERR'] for m in maps])
        self.xera, self.yera = None, None
        self.xerb, self.yerb = None, None


    def replace_unseen(self, map_data):
        # Replace hp.UNSEEN values with np.nan
        map_data[map_data == hp.UNSEEN] = np.nan
        return map_data

    def Aperture(self, lon , lat, phi, theta, a, b=None, pang=0., frac=0., sweep=360., bkgd=False):
        '''
        lon    - longitude of pixel coordinates
        lat    - latitude of pixel coordinates

        phi    - longitude of aperture
        theta  - latitude of aperture
        a      - major-axis
        b      - minor-axis
        pang   - rotation angle of aperture
        frac   - ratio between inner and outer axes
        sweep  - angular sweep of aperture

        Returns:
        array of pixels that are within the aperture
        '''



        if isinstance(b, type(None)) or not b:
            b = a

        # Convert to a projected cartesian grid
        x = np.cos(lon*d2r)*np.cos(lat*d2r)
        y = np.sin(lon*d2r)*np.cos(lat*d2r)
        z = np.sin(lat*d2r)

        # Rotate to be centred on source
        xr, yr, zr = rotatelon(x , y , z , phi*d2r)
        xr, yr, zr = rotatelat(xr, yr, zr, -(90.-theta)*d2r)
        xr, yr, zr = rotatelon(xr, yr, zr, pang*d2r)
        xr /= d2r
        yr /= d2r
        zr /= d2r


        # Convert to a projected cartesian grid
        if isinstance(self.xera, type(None)):
            ang = np.linspace(0, 2*np.pi, 360*2)
            xe = a*np.cos(ang)
            ye = b*np.sin(ang)
            xo = a*np.cos(ang)*frac
            yo = b*np.sin(ang)*frac

            self.xera, self.yera = [], []
            self.xera += [( np.cos((90-pang)*d2r)*xe + np.sin((90-pang)*d2r)*ye) + phi]
            self.yera += [(-np.sin((90-pang)*d2r)*xe + np.cos((90-pang)*d2r)*ye) + theta]
            self.xera[0] *= d2r
            self.yera[0] = (90. - self.yera[0])*d2r

            self.xera += [( np.cos((90-pang)*d2r)*xo + np.sin((90-pang)*d2r)*yo) + phi]
            self.yera += [(-np.sin((90-pang)*d2r)*xo + np.cos((90-pang)*d2r)*yo) + theta]
            self.xera[1] *= d2r
            self.yera[1] = (90. - self.yera[1])*d2r


        elif isinstance(self.xerb, type(None)) & bkgd:
            ang = np.linspace(0, 2*np.pi, 360*2)
            xe = a*np.cos(ang)
            ye = b*np.sin(ang)
            xo = a*np.cos(ang)*frac
            yo = b*np.sin(ang)*frac

            self.xerb, self.yerb = [], []
            self.xerb += [( np.cos((90-pang)*d2r)*xe + np.sin((90-pang)*d2r)*ye) + phi]
            self.yerb += [(-np.sin((90-pang)*d2r)*xe + np.cos((90-pang)*d2r)*ye) + theta]
            self.xerb[0] *= d2r
            self.yerb[0] = (90. - self.yerb[0])*d2r

            self.xerb += [( np.cos((90-pang)*d2r)*xo + np.sin((90-pang)*d2r)*yo) + phi]
            self.yerb += [(-np.sin((90-pang)*d2r)*xo + np.cos((90-pang)*d2r)*yo) + theta]
            self.xerb[1] *= d2r
            self.yerb[1] = (90. - self.yerb[1])*d2r


        ilon = np.arctan2(yr*d2r, xr*d2r)/d2r

        # Now use conditionals to calculate aperture
        gd  = ((xr/a)**2 + (yr/b)**2 < 1**2) & (zr > 0) # (zr > 0) so we only get one aperture
        agd = (ilon > -180) & (ilon < sweep-180.)
        if frac != 0:
            fgd = ((xr/a/frac)**2 + (yr/b/frac)**2 > 1**2)
        else:
            fgd = True

        return np.where((gd & agd & fgd))[0]

    def planckcorr(self, nu_in):
        '''
        Expects nu in GHz
        '''
        c = 299792458.
        k = 1.3806488e-23
        h = 6.62606957e-34
        T_cmb = 2.725

        nu = nu_in * 1e9

        x = h*nu/k/T_cmb

        return x**2*np.exp(x)/(np.exp(x) - 1.)**2

    def toJy(self,nu, beam):
        '''
        '
        nu - in GHz
        beam - in steradians
        '''
        c = 299792458.
        k = 1.3806488e-23

        jy = 2 * k   * (nu*1e9)**2/ c**2 * beam * 1e26

        return jy

    def Units(self, mapinfo):
        '''
        '
        Pass a self.map value and it will convert map to Jy/pix
        '''

        nu = mapinfo['frequency']
        pixbeam = 4.*np.pi/(12.*mapinfo['nside']**2)
        conversions = {'K':1.*self.toJy(nu, pixbeam),
                       'mK_RJ':1e-3*self.toJy(nu, pixbeam),
                       'mK':1e-3*self.toJy(nu, pixbeam),
                       'mKCMB':self.planckcorr(nu)*1e-3*self.toJy(nu, pixbeam),
                       'KCMB':self.planckcorr(nu)*self.toJy(nu, pixbeam),
                       'MJysr':1e6*pixbeam}

        return conversions[mapinfo['unit']]


    def AperPhot(self, _lon, _lat, target, mode='median', throw_NaN=True, scale_random_noise_by_beam_area=False, effective_beam_area=1.13309003546, rescale_random_errors=None):
        '''
        lon    - 'longitude of pixel coordinates''
        lat    - latitude of pixel coordinates
        target - aperture photometry target information
        '''

        import config_phot


        import os   # Make source-specific directory
        if not os.path.exists('{}/{}'.format(saveAperdir,target['name'])):
            os.makedirs('{}/{}'.format(saveAperdir,target['name']))


        # Loop through apertures

        nApertures = len(target['phi'])
        self.aperPix = [[self.Aperture(_lon[j], _lat[j],
                                   target['phi'][i], target['theta'][i],
                                   target['ra'][i], b=target['rb'][i],
                                   pang=target['pang'][i], frac=target['frac'][i]) for i in range(nApertures)] for j in range(len(_lon))]

        nPix = [ len(np.unique(np.concatenate(self.aperPix[i]))) for i in range(len(_lon))]


        # Second loop through backgrounds

        nBackgrounds = len(target['iphi'])
        self.bkgdPix = [[self.Aperture(_lon[j], _lat[j],
                                 target['iphi'][i], target['itheta'][i],
                                 target['ira'][i], b=target['irb'][i],
                                 pang=target['ipang'][i], frac=target['ifrac'][i],
                                 sweep=target['isweep'][i], bkgd=True) for i in range(nBackgrounds)] for j in range(len(_lon))]



        # Loop over fluxes and backgrounds

        aperFluxes  = np.zeros((len(self.data), len(self.aperPix)))
        bkgdFluxes_median  = np.zeros((len(self.data), len(self.bkgdPix))) # for median calculations
        bkgdFluxes  = np.zeros((len(self.data), len(self.bkgdPix)))
        bkgd2Fluxes = np.zeros((len(self.data), len(self.bkgdPix)))
        flux = np.zeros(len(self.data))
        err  = np.zeros(len(self.data))


        for j in range(len(self.data)):
            cfac = self.Units(self.maps[j])
            pixType = int(np.where((self.unpix == self.npixs[j]))[0])

            # # Uncomment below if you want to actually see the location of the background apertures
            # self.data[j][self.bkgdPix[pixType][0]] = 0
            # self.data[j][self.bkgdPix[pixType][1]] = 0
            # import healpy as hp
            # import matplotlib.pyplot as plt
            # hp.gnomview(self.data[j],rot=[-164.3, -11.6],reso=5)
            # plt.show()

            if throw_NaN==True:

                for i in range(len(self.aperPix[pixType])):
                    aperFluxes[j,i] =  np.sum(self.data[j][self.aperPix[pixType][i]])*cfac # changed from nansum to sum

                if mode=='median':
                    for i in range(len(self.bkgdPix[pixType])):
                        bkgdFluxes_median[j,i]  = np.median(self.data[j][self.bkgdPix[pixType][i]])*cfac # changed from nanmedian to median
                        bkgdFluxes[j,i]  = np.mean(self.data[j][self.bkgdPix[pixType][i]])*cfac # changed from nanmedian to median
                        bkgd2Fluxes[j,i] = np.mean(self.data[j][self.bkgdPix[pixType][i]]**2)*cfac**2 # changed from nanmedian to median
                if mode=='mean':
                    for i in range(len(self.bkgdPix[pixType])):
                        bkgdFluxes[j,i]  = np.mean(self.data[j][self.bkgdPix[pixType][i]])*cfac # changed from nanmedian to median
                        bkgd2Fluxes[j,i] = np.mean(self.data[j][self.bkgdPix[pixType][i]]**2)*cfac**2 # changed from nanmedian to median


            elif throw_NaN==False:

                for i in range(len(self.aperPix[pixType])):
                    aperFluxes[j,i] =  np.nansum(self.data[j][self.aperPix[pixType][i]])*cfac

                # Work out background properties
                for i in range(len(self.bkgdPix[pixType])):
                    bkgdFluxes_median[j,i]  = np.nanmedian(self.data[j][self.bkgdPix[pixType][i]])*cfac # changed from nanmedian to median
                    bkgdFluxes[j,i]  = np.nanmean(self.data[j][self.bkgdPix[pixType][i]])*cfac
                    bkgd2Fluxes[j,i] = np.nanmean(self.data[j][self.bkgdPix[pixType][i]]**2)*cfac**2

                if mode=='mean': # if mode is mean, turn the median into a mean, otherwise median by default
                    bkgdFluxes_median = bkgdFluxes


            indices_to_use = np.array(np.where(bkgdFluxes[j,:]!=0),dtype=int)
            '''
            Above "indices_to_use" is there because that way we only select backgrounds that have
            been measured (i.e. if only one background out of three possible ones has been entered,
            then take the average only accross that one column that is filled, not all three!).
            Here below the code adds these multiple primaries or backgrounds that have been selected.
            '''

            # TODO: in the case of including NaN, we need to scale the fluxes by a factor NPix_total/NPix_notnan in order to account for the missing flux
            # TODO: revise error calculations below because the error in the flux, which comes from the calibration of the map and the backgrounds, is only
            # taking into account the rms between several backgrounds rather than the rms in each!

            if throw_NaN==True:
                flux[j] = np.sum(aperFluxes[j,:]) - np.mean(bkgdFluxes_median[j,indices_to_use]) * nPix[pixType]
                random_var = (np.mean(bkgd2Fluxes[j,indices_to_use]) - np.mean(bkgdFluxes[j,indices_to_use])**2 )*nPix[pixType]

            elif throw_NaN==False:
                flux[j] = np.nansum(aperFluxes[j,:]) - np.nanmean(bkgdFluxes_median[j,indices_to_use]) * nPix[pixType]
                random_var = (np.nanmean(bkgd2Fluxes[j,indices_to_use]) - np.nanmean(bkgdFluxes[j,indices_to_use])**2 )*nPix[pixType]

            # Calibration variance
            calibration_var = (flux[j]*self.calerr[j])**2

            # Scale the random variance by the beam resolution, since independent pixels are at FWHM = 1 so the sqrt(npix) scaling is a low estimate
            if scale_random_noise_by_beam_area:

                # Get number of pixels in primary aperture
                nPix[pixType] = nPix[pixType]

                # Get number of beams in primary aperture
                primary_area_deg2 = target['primary_sol_ang_sr']*(180/np.pi)**2
                nPix_independent = primary_area_deg2/effective_beam_area

                # print(f'{primary_area_deg2:.1f}/{effective_beam_area:.2f} = {nPix_independent:.1f} independent pixels instead of {nPix[pixType]} pix, so noise underestimated by a factor of {np.sqrt(nPix[pixType]/nPix_independent):.1f}')

                # Scale the random noise accordingly
                random_var = random_var * (nPix[pixType]/nPix_independent)


            # Rescale random errors if the setting is toggled
            if rescale_random_errors is not None:
                random_var = random_var*(rescale_random_errors**2) # square to scale variance correctly



            # Add up the variances to get the total variance from which the final error is calculated
            err[j] = random_var + calibration_var # This is the variance, so at the end the sqrt is returned for a standard deviation




            # print(f'{self.nu[j]:.1f} GHz, '
            #       f'flux = {flux[j]:.4f}, '
            #       f'total_err = {np.sqrt(err[j]):.4f}, '
            #       f'random_err = {np.sqrt((np.mean(bkgd2Fluxes[j,indices_to_use]) - np.mean(bkgdFluxes[j,indices_to_use])**2 )*nPix[pixType]):.4f}, '
            #       f'ran_1 = {np.mean(bkgd2Fluxes[j,indices_to_use]):.4f}, '
            #       f'ran_2 = {np.mean(bkgdFluxes[j,indices_to_use])**2}, '
            #       f'calibration_err = {np.sqrt((flux[j]*self.calerr[j])**2):.4f}')
            # # print(f"Data slice for iteration {j}, index {i}: {self.data[j][self.bkgdPix[pixType][i]]}")



            # PLOT APERTURES AND HISTOGRAMS OF THE BACKGROUND

            if save_aper == True:

                try:
                    # Ensure the directory exists
                    apertures_dir = '{}/{}/apertures'.format(saveAperdir, target['name'])
                    os.makedirs(apertures_dir, exist_ok=True)  # Creates the directory if it doesn't exist

                    plt.figure(1)

                    projected_map = hp.gnomview(
                        self.data[j],
                        rot=[target['phi'][0], target['theta'][0]],
                        reso=1,
                        xsize=400,
                        cmap=plt.get_cmap('viridis'),
                        fig=1,
                        title=self.maps[j]['name'].split('/')[-1],
                        return_projected_map=True
                    )
                    plt.clf()

                    hp.gnomview(
                        self.data[j],
                        rot=[target['phi'][0], target['theta'][0]],
                        reso=1,
                        xsize=400,
                        cmap=plt.get_cmap('viridis'),
                        min=np.nanmin(projected_map),
                        max=np.nanmax(projected_map),
                        fig=1,
                        title=self.maps[j]['name'].split('/')[-1],
                        return_projected_map=True
                    )

                    hp.projplot(self.yera[0], self.xera[0], '.', color='b', markersize=0.5)
                    hp.projplot(self.yera[1], self.xera[1], '.', color='b', markersize=0.5)
                    hp.projplot(self.yerb[0], self.xerb[0], '.', color='r', markersize=0.5)
                    hp.projplot(self.yerb[1], self.xerb[1], '.', color='r', markersize=0.5)

                    plt.show()
                    plt.savefig('{}/{:02d}_primary.png'.format(apertures_dir, j))
                    plt.clf()

                    # Plot background aperture
                    background1 = self.data[j][self.bkgdPix[pixType][i]]
                    background1 = background1[~np.isnan(background1)]

                    hp.gnomview(
                        self.data[j],
                        rot=[target['phi'][0], target['theta'][0]],
                        reso=1,
                        xsize=400,
                        cmap=plt.get_cmap('viridis'),
                        min=np.nanmin(background1) / 2.0,
                        max=np.nanmax(background1) * 2.0,
                        fig=1,
                        title=self.maps[j]['name'].split('/')[-1],
                        return_projected_map=True
                    )

                    hp.projplot(self.yera[0], self.xera[0], '.', color='b', markersize=0.5)
                    hp.projplot(self.yera[1], self.xera[1], '.', color='b', markersize=0.5)
                    hp.projplot(self.yerb[0], self.xerb[0], '.', color='r', markersize=0.5)
                    hp.projplot(self.yerb[1], self.xerb[1], '.', color='r', markersize=0.5)

                    #plt.savefig('{}/{:02d}_background.png'.format(apertures_dir, j))
                    plt.clf()

                except Exception as e:
                    print('Could not produce aperture plot of {}: {}'.format(self.maps[j]['name'], e))



                    # Histogram the data

                    if save_hist == True:

                        try:

                            background1 = self.data[j][self.bkgdPix[pixType][i]]
                            background1 = background1[~np.isnan(background1)]

                            plt.figure(4)
                            n, bins, patches = plt.hist(background1,int(len(background1)/10.0),histtype='step')
                            plt.clf()
                            bins = [(bins[i+1]+bins[i])/2.0 for i in range(0,len(bins)-1)]
                            plt.fill_between(bins,n,color='r',alpha=0.6)
                            plt.ylim([0,np.nanmax(n)*1.1])
                            plt.axvline(x=np.nanmedian(background1),color='r',linestyle='--')
                            plt.axvline(x=np.nanmedian(background1)+np.nanstd(background1),color='r',linestyle='--')
                            plt.axvline(x=np.nanmedian(background1)-np.nanstd(background1),color='r',linestyle='--')
                            plt.title("{} Background [{} GHz]".format(target['name'],self.maps[j]['frequency']))

                            plt.savefig('{}/{}/{:02d}_hist.png'.format(saveAperdir,target['name'], j))

                            plt.clf()

                        except:

                            print('Could not produce histogram of {}'.format(self.maps[j]['name']))

        if rescale_random_errors is not None:
            print(f"Multiplied random photometry errors by {rescale_random_errors}.")


        # Ensure the directory exists
        apertures_dir = '{}/{}/apertures'.format(save_fluxes, target['name'])
        os.makedirs(apertures_dir, exist_ok=True)  # Creates the directory if it doesn't exist

        # Save results to folder
        np.savetxt('{}/fluxes.dat'.format(apertures_dir), [self.nu, flux, np.sqrt(err)])

        # Save aperture settings to folder
        with open('{}/aperture_settings.dat'.format(apertures_dir), 'w') as text_file:
            print(target, file=text_file)



        return flux, np.sqrt(err), self.nu
