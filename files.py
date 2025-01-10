# List all the input files to be processed

import numpy as np
import bandpasses


## Config

'''
beam_eff_err accounts for the discrepancy between the beam-scale and large-scale calibration due to low beam efficiencies,
which affects the haslam, dwingeloo and reich maps resulting in an error of up to a factor of 2
'''

beam_eff_err = 0.3  # accounts for up to 30% beam efficiency error in a flux density measurement - only for haslam, dwingeloo and Reich



## Maps

# Low-Frequency (0.408-5 GHz) Maps

haslam = {'name':'/home/rcepeda/Desktop/data/ancillary_data/CMBon/haslam408_ds_smth.fits',
          'inst':'HASLAM',
          'frequency':0.408,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'K',
          'nside':512,
          'fmt':'o',
          'color':'#F29900',
          'CALERR':(0.1**2+beam_eff_err**2)**0.5}

dwingeloo = {'name':'/home/rcepeda/Desktop/data/ancillary_data/CMBon/dwingeloo_820.fits',
          'inst':'Dwingeloo',
          'frequency':0.820,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'K',
          'nside':128,
          'fmt':'o',
          'color':'#F29900',
          'CALERR':(0.1**2+beam_eff_err**2)**0.5}

Reich = {'name':'/home/rcepeda/Desktop/data/ancillary_data/CMBon/512_60.00smoothed_reichlb21_1.42_512_1986.fits',
         'inst':'Reich',
         'frequency':1.42,
         'resolution':1.1331*(np.pi/180.)**2,
         'unit':'mK',
         'nside':512,
         'fmt':'o',
         'color':'#31D63F',
         'CALERR':(0.05**2+beam_eff_err**2)**0.5}


Reich_rescaled_calibration = {'name':'/home/rcepeda/Desktop/data/ancillary_data/CMBon/512_60.00smoothed_reichlb21_1.42_512_1986_rescaled_multiplied_by_155_pointsources.fits',
         'inst':'Reich',
         'frequency':1.42,
         'resolution':1.1331*(np.pi/180.)**2,
         'unit':'mK',
         'nside':512,
         'fmt':'o',
         'color':'#31D63F',
         'CALERR':(0.05**2+beam_eff_err**2)**0.5}




Jonas = {'name':'/home/rcepeda/Desktop/data/ancillary_data/others/512_60.00smoothed_jonas98_2.326_512_1998_K.fits',
         'inst':'Jonas',
         'frequency':2.326,
         'resolution':1.1331*(np.pi/180.)**2,
         'unit':'K',
         'nside':512,
         'fmt':'o',
         'color':'#31D63F',
         'CALERR':0.10}

Jonas_Lambda_Orionis = {'name':'/home/rcepeda/Desktop/data/ancillary_data/others/Jonas_cropped_lambda_orionis.fits',
         'inst':'Jonas',
         'frequency':2.326,
         'resolution':1.1331*(np.pi/180.)**2,
         'unit':'K',
         'nside':512,
         'fmt':'o',
         'color':'#31D63F',
         'CALERR':0.10} # this needs a beam effective error too!!


# SPASS goes here
spass = {'name':'/home/rcepeda/Desktop/data/spass/spass_dr1_1902_healpix_Tb.i_smoothed_1deg_nside512_2303MHz.fits',
         'inst':'S-PASS',
         'frequency':2.303,
         'resolution':1.1331*(np.pi/180.)**2,
         'unit':'K',
         'nside':512,
         'fmt':'o',
         'color':'#31D63F',
         'CALERR':0.05}



# CBASS maps

CBASS = {'name':'/home/rcepeda/Desktop/data/cbass/science_maps/v28allels/NIGHTMERID20/filtered_map/tauA_cal_NIGHTMERID20_v28allelsNs_ALL_NIGHTMERID20_noiseCut_masked5pc_G_1024_ol500_lessTol_g_map_g_1deg_0512_wiener.fits',
          'inst':'C-BASS',
          'frequency':4.76,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'K',
          'nside':512,
          'fmt':'o',
          'color':'#FDE5E5',
          'CALERR':0.03}

CBASS_NEW = {'name':'/home/rcepeda/Desktop/data/cbass/v33b_deconvolution_oldbeam/oldBeam_tauA_cal_NM20_v33b_allelsNS1_xAS14_masked5pc_C_1024_ol500_lessTol_g_Pipe_map_1024.fits',
          'inst':'C-BASS',
          'frequency':4.76,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'K',
          'nside':1024,
          'fmt':'o',
          'color':'#FDE5E5',
          'CALERR':0.03}

# BELOW RICHARD'S MAP BUT WITH THE NEW BEAM DECONVOLUTION
CBASS_early_DR1 = {'name':'/home/rcepeda/Desktop/data/cbass/cbass_DR1_NEWBEAM_deconvolved_01deg_1024_G_intensity.fits',
          'inst':'C-BASS',
          'frequency':4.76,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'K',
          'nside':1024,
          'fmt':'o',
          'color':'#FDE5E5',
          'CALERR':0.03}



# QUIJOTE Data Release

quijote11_datarelease = {'name':'/home/rcepeda/Desktop/data/quijote/QUIJOTE-MFI-Release1/quijote_mfi_smth_skymap_11ghz_512_dr1.fits',
                         'inst':'MFI',
                         'frequency': 11.1,
                         'resolution':1.1331*(np.pi/180.)**2,
                         'unit':'mKCMB',
                         'nside':512,
                         'bandpass':bandpasses.fastmficc, # TODO UPDATE THESE -- NOT APPLIED AT THE MOMENT
                         'fmt':'*',
                         'color':'#9900F2',
                         'CALERR':0.05}

quijote13_datarelease = {'name':'/home/rcepeda/Desktop/data/quijote/QUIJOTE-MFI-Release1/quijote_mfi_smth_skymap_13ghz_512_dr1.fits',
                         'inst':'MFI',
                         'frequency': 12.9,
                         'resolution':1.1331*(np.pi/180.)**2,
                         'unit':'mKCMB',
                         'nside':512,
                         'bandpass':bandpasses.fastmficc, # TODO UPDATE THESE -- NOT APPLIED AT THE MOMENT
                         'fmt':'*',
                         'color':'#9900F2',
                         'CALERR':0.05}

quijote17_datarelease = {'name':'/home/rcepeda/Desktop/data/quijote/QUIJOTE-MFI-Release1/quijote_mfi_smth_skymap_17ghz_512_dr1.fits',
                         'inst':'MFI',
                         'frequency': 16.8,
                         'resolution':1.1331*(np.pi/180.)**2,
                         'unit':'mKCMB',
                         'nside':512,
                         'bandpass':bandpasses.fastmficc, # TODO UPDATE THESE -- NOT APPLIED AT THE MOMENT
                         'fmt':'*',
                         'color':'#9900F2',
                         'CALERR':0.05}

quijote19_datarelease = {'name':'/home/rcepeda/Desktop/data/quijote/QUIJOTE-MFI-Release1/quijote_mfi_smth_skymap_19ghz_512_dr1.fits',
                         'inst':'MFI',
                         'frequency': 18.8,
                         'resolution':1.1331*(np.pi/180.)**2,
                         'unit':'mKCMB',
                         'nside':512,
                         'bandpass':bandpasses.fastmficc, # TODO UPDATE THESE -- NOT APPLIED AT THE MOMENT
                         'fmt':'*',
                         'color':'#9900F2',
                         'CALERR':0.05}



# Old QUIJOTE maps below

quijote11_nov2019 = {'name':'/home/rcepeda/Desktop/data/quijote/release_nov2019/quijote_1deg_11GHz.fits',
             'inst':'MFI',
             'frequency':11.19, # CHANGE THESE TO EFFECTIVE FREQUENCIES CHOSEN
             'resolution':1.1331*(np.pi/180.)**2,
             'unit':'K',
             'nside':512,
             'bandpass':bandpasses.fastmficc,
             'fmt':'*',
             'color':'#9900F2',
             'CALERR':0.03}

quijote11_NEW = {'name':'/home/rcepeda/Desktop/data/quijote/Feb2020/quijote_1deg_11GHz.fits',
             'inst':'MFI',
             'frequency':11.19, # CHANGE THESE TO EFFECTIVE FREQUENCIES CHOSEN
             'resolution':1.1331*(np.pi/180.)**2,
             'unit':'K',
             'nside':512,
             'bandpass':bandpasses.fastmficc,
             'fmt':'*',
             'color':'#9900F2',
             'CALERR':0.03}

quijote13_nov2019 = {'name':'/home/rcepeda/Desktop/data/quijote/release_nov2019/quijote_1deg_13GHz.fits',
              'inst':'MFI',
              'frequency':12.86,
              'resolution':1.1331*(np.pi/180.)**2,
              'unit':'K',
              'nside':512,
              'bandpass':bandpasses.fastmficc,
              'fmt':'*',
              'color':'#9900F2',
              'CALERR':0.03}

quijote13_NEW = {'name':'/home/rcepeda/Desktop/data/quijote/Feb2020/quijote_1deg_13GHz.fits',
              'inst':'MFI',
              'frequency':12.86,
              'resolution':1.1331*(np.pi/180.)**2,
              'unit':'K',
              'nside':512,
              'bandpass':bandpasses.fastmficc,
              'fmt':'*',
              'color':'#9900F2',
              'CALERR':0.03}

quijote17_nov2019 = {'name':'/home/rcepeda/Desktop/data/quijote/release_nov2019/quijote_1deg_17GHz.fits',
              'inst':'MFI',
              'frequency':16.75,
              'resolution':1.1331*(np.pi/180.)**2,
              'unit':'K',
              'nside':512,
              'bandpass':bandpasses.fastmficc,
              'fmt':'*',
              'color':'#9900F2',
              'CALERR':0.18}

quijote17_NEW = {'name':'/home/rcepeda/Desktop/data/quijote/Feb2020/quijote_1deg_17GHz.fits',
              'inst':'MFI',
              'frequency':16.75,
              'resolution':1.1331*(np.pi/180.)**2,
              'unit':'K',
              'nside':512,
              'bandpass':bandpasses.fastmficc,
              'fmt':'*',
              'color':'#9900F2',
              'CALERR':0.18}

quijote19_nov2019 = {'name':'/home/rcepeda/Desktop/data/quijote/release_nov2019/quijote_1deg_19GHz.fits',
             'inst':'MFI',
             'frequency':18.71,
             'resolution':1.1331*(np.pi/180.)**2,
             'unit':'K',
             'nside':512,
             'bandpass':bandpasses.fastmficc,
             'fmt':'*',
             'color':'#9900F2',
             'CALERR':0.28}

quijote19_NEW = {'name':'/home/rcepeda/Desktop/data/quijote/Feb2020/quijote_1deg_19GHz.fits',
             'inst':'MFI',
             'frequency':18.71,
             'resolution':1.1331*(np.pi/180.)**2,
             'unit':'K',
             'nside':512,
             'bandpass':bandpasses.fastmficc,
             'fmt':'*',
             'color':'#9900F2',
             'CALERR':0.28}


# # Roke's 1 degree smoothed files
#
# quijote11 = {'name':'/home/rcepeda/Desktop/data/ancillary_data/CMBoff/calibrated_smth_11GHz.fits',
#              'inst':'MFI',
#              'frequency':11.,
#              'resolution':1.1331*(np.pi/180.)**2,
#              'unit':'K',
#              'nside':512,
#              'bandpass':bandpasses.fastmficc,
#              'fmt':'*',
#              'color':'#9900F2',
#              'CALERR':0.05}
#
# quijote13 = {'name':'/home/rcepeda/Desktop/data/ancillary_data/CMBoff/calibrated_smth_13GHz.fits',
#               'inst':'MFI',
#               'frequency':13.,
#               'resolution':1.1331*(np.pi/180.)**2,
#               'unit':'K',
#               'nside':512,
#               'bandpass':bandpasses.fastmficc,
#               'fmt':'*',
#               'color':'#9900F2',
#               'CALERR':0.05}
#
# quijote17 = {'name':'/home/rcepeda/Desktop/data/ancillary_data/CMBoff/calibrated_smth_17GHz.fits',
#               'inst':'MFI',
#               'frequency':17.,
#               'resolution':1.1331*(np.pi/180.)**2,
#               'unit':'K',
#               'nside':512,
#               'bandpass':bandpasses.fastmficc,
#               'fmt':'*',
#               'color':'#9900F2',
#               'CALERR':0.18}
#
# quijote19 = {'name':'/home/rcepeda/Desktop/data/ancillary_data/CMBoff/calibrated_smth_19GHz.fits',
#              'inst':'MFI',
#              'frequency':19.,
#              'resolution':1.1331*(np.pi/180.)**2,
#              'unit':'K',
#              'nside':512,
#              'bandpass':bandpasses.fastmficc,
#              'fmt':'*',
#              'color':'#9900F2',
#              'CALERR':0.28}
#
#
# # # Roke's 1 degree smoothed files
#
# quijote11 = {'name':'/home/rcepeda/Desktop/data/quijote/old_versions/release_jul_2019/quijote_release_healpy_11GHz.fits',
#              'inst':'MFI',
#              'frequency':11.,
#              'resolution':1.1331*(np.pi/180.)**2,
#              'unit':'K',
#              'nside':512,
#              'bandpass':bandpasses.fastmficc,
#              'fmt':'*',
#              'color':'#9900F2',
#              'CALERR':0.05}
#
# quijote13 = {'name':'/home/rcepeda/Desktop/data/quijote/old_versions/release_jul_2019/quijote_release_healpy_13GHz.fits',
#               'inst':'MFI',
#               'frequency':13.,
#               'resolution':1.1331*(np.pi/180.)**2,
#               'unit':'K',
#               'nside':512,
#               'bandpass':bandpasses.fastmficc,
#               'fmt':'*',
#               'color':'#9900F2',
#               'CALERR':0.05}
#
# quijote17 = {'name':'/home/rcepeda/Desktop/data/quijote/old_versions/release_jul_2019/quijote_release_healpy_17GHz.fits',
#               'inst':'MFI',
#               'frequency':17.,
#               'resolution':1.1331*(np.pi/180.)**2,
#               'unit':'K',
#               'nside':512,
#               'bandpass':bandpasses.fastmficc,
#               'fmt':'*',
#               'color':'#9900F2',
#               'CALERR':0.18}
#
# quijote19 = {'name':'/home/rcepeda/Desktop/data/quijote/old_versions/release_jul_2019/quijote_release_healpy_19GHz.fits',
#              'inst':'MFI',
#              'frequency':19.,
#              'resolution':1.1331*(np.pi/180.)**2,
#              'unit':'K',
#              'nside':512,
#              'bandpass':bandpasses.fastmficc,
#              'fmt':'*',
#              'color':'#9900F2',
#              'CALERR':0.28}


#
#
# quijote11rhooph = {'name':'/home/rcepeda/Desktop/data/ancillary_data/CMBon/CAL-RHOOPH-11GHz.fits',
#              'inst':'MFI',
#              'frequency':11.,
#              'resolution':1.1331*(np.pi/180.)**2,
#              'unit':'K',
#              'nside':512,
#              'bandpass':bandpasses.fastmficc,
#              'fmt':'*',
#              'color':'#9900F2',
#              'CALERR':0.10}
#
# quijote13rhooph = {'name':'/home/rcepeda/Desktop/data/ancillary_data/CMBon/CAL-RHOOPH-13GHz.fits',
#               'inst':'MFI',
#               'frequency':13.,
#               'resolution':1.1331*(np.pi/180.)**2,
#               'unit':'K',
#               'nside':512,
#               'bandpass':bandpasses.fastmficc,
#               'fmt':'*',
#               'color':'#9900F2',
#               'CALERR':0.10}
#
#
# quijote17rhooph = {'name':'/home/rcepeda/Desktop/data/ancillary_data/CMBon/UNCAL-RHOOPH-17GHz.fits',
#              'inst':'MFI',
#              'frequency':17.,
#              'resolution':1.1331*(np.pi/180.)**2,
#              'unit':'K',
#              'nside':512,
#              'bandpass':bandpasses.fastmficc,
#              'fmt':'*',
#              'color':'#9900F2',
#              'CALERR':0.1}
#
# quijote19rhooph = {'name':'/home/rcepeda/Desktop/data/ancillary_data/CMBon/UNCAL-RHOOPH-19GHz.fits',
#               'inst':'MFI',
#               'frequency':19.,
#               'resolution':1.1331*(np.pi/180.)**2,
#               'unit':'K',
#               'nside':512,
#               'bandpass':bandpasses.fastmficc,
#               'fmt':'*',
#               'color':'#9900F2',
#               'CALERR':0.1}




# WMAP and Planck


wmapK = {'name':'/home/rcepeda/Desktop/data/ancillary_data/CMBoff/wmap_band_smth_imap_r9_9yr_K_v5.fits',
        'inst':'WMAP',
        'frequency':22.8,
        'resolution':1.1331*(np.pi/180.)**2,
        'unit':'mKCMB',
        'nside':512,
        'fmt':'o',
        'bandpass':bandpasses.fastwmapcc,
        'CALERR':0.01,
        'color':'#0059F2'}

wmapK_cosmoglobe = {'name':'/home/rcepeda/Desktop/data/cosmoglobe/processed/023-WMAP_K_1deg_nside512_CMBoff_KCMB.fits',
        'inst':'WMAP',
        'frequency':22.8,
        'resolution':1.1331*(np.pi/180.)**2,
        'unit':'KCMB',
        'nside':512,
        'fmt':'o',
        'bandpass':bandpasses.fastwmapcc,
        'CALERR':0.01,
        'color':'#0059F2'}


wmapKa = {'name':'/home/rcepeda/Desktop/data/ancillary_data/CMBoff/wmap_band_smth_imap_r9_9yr_Ka_v5.fits',
         'inst':'WMAP',
         'frequency':33.,
         'resolution':1.1331*(np.pi/180.)**2,
         'unit':'mKCMB',
         'nside':512,
         'fmt':'o',
         'bandpass':bandpasses.fastwmapcc,
         'CALERR':0.01,
         'color':'#0059F2'}

wmapKa_cosmoglobe = {'name':'/home/rcepeda/Desktop/data/cosmoglobe/processed/030-WMAP_Ka_1deg_nside512_CMBoff_KCMB.fits',
         'inst':'WMAP',
         'frequency':33.,
         'resolution':1.1331*(np.pi/180.)**2,
         'unit':'KCMB',
         'nside':512,
         'fmt':'o',
         'bandpass':bandpasses.fastwmapcc,
         'CALERR':0.01,
         'color':'#0059F2'}


wmapQ = {'name':'/home/rcepeda/Desktop/data/ancillary_data/CMBoff/wmap_band_smth_imap_r9_9yr_Q_v5.fits',
         'inst':'WMAP',
         'frequency':40.7,
         'resolution':1.1331*(np.pi/180.)**2,
         'unit':'mKCMB',
         'nside':512,
         'fmt':'o',
         'bandpass':bandpasses.fastwmapcc,
         'CALERR':0.01,
         'color':'#0059F2'}

wmapQ_cosmoglobe = {'name':'/home/rcepeda/Desktop/data/cosmoglobe/processed/040-WMAP_Q_1deg_nside512_CMBoff_KCMB.fits',
         'inst':'WMAP',
         'frequency':40.7,
         'resolution':1.1331*(np.pi/180.)**2,
         'unit':'KCMB',
         'nside':512,
         'fmt':'o',
         'bandpass':bandpasses.fastwmapcc,
         'CALERR':0.01,
         'color':'#0059F2'}


wmapV = {'name':'/home/rcepeda/Desktop/data/ancillary_data/CMBoff/wmap_band_smth_imap_r9_9yr_V_v5.fits',
         'inst':'WMAP',
         'frequency':60.7,
         'resolution':1.1331*(np.pi/180.)**2,
         'unit':'mKCMB',
         'nside':512,
         'fmt':'o',
         'bandpass':bandpasses.fastwmapcc,
         'CALERR':0.01,
         'color':'#0059F2'}

wmapV_cosmoglobe = {'name':'/home/rcepeda/Desktop/data/cosmoglobe/processed/060-WMAP_V_1deg_nside512_CMBoff_KCMB.fits',
         'inst':'WMAP',
         'frequency':60.7,
         'resolution':1.1331*(np.pi/180.)**2,
         'unit':'KCMB',
         'nside':512,
         'fmt':'o',
         'bandpass':bandpasses.fastwmapcc,
         'CALERR':0.01,
         'color':'#0059F2'}


wmapW = {'name':'/home/rcepeda/Desktop/data/ancillary_data/CMBoff/wmap_band_smth_imap_r9_9yr_W_v5.fits',
         'inst':'WMAP',
         'frequency':93.6,
         'resolution':1.1331*(np.pi/180.)**2,
         'unit':'mKCMB',
         'nside':512,
         'fmt':'o',
         'bandpass':bandpasses.fastwmapcc,
         'CALERR':0.01,
         'color':'#0059F2'}

wmapW_cosmoglobe = {'name':'/home/rcepeda/Desktop/data/cosmoglobe/processed/090-WMAP_W_1deg_nside512_CMBoff_KCMB.fits',
         'inst':'WMAP',
         'frequency':93.6,
         'resolution':1.1331*(np.pi/180.)**2,
         'unit':'KCMB',
         'nside':512,
         'fmt':'o',
         'bandpass':bandpasses.fastwmapcc,
         'CALERR':0.01,
         'color':'#0059F2'}


lfi30 = {'name':'/home/rcepeda/Desktop/data/ancillary_data/CMBoff/LFI_SkyMap_30_512_smth.fits',
          'inst':'Planck',
          'frequency':28.4,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'KCMB',
          'bandpass':bandpasses.fastlficc,
          'nside':512,
          'fmt':'s',
          'CALERR':0.01,
          'color':'#59F200'}

lfi30_npipe = {'name':'/home/rcepeda/Desktop/data/npipe/processed/npipe6v20_030_1deg_nside512_CMBoff_KCMB.fits',
          'inst':'Planck',
          'frequency':28.4,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'KCMB',
          'bandpass':bandpasses.fastlficc,
          'nside':512,
          'fmt':'s',
          'CALERR':0.01,
          'color':'#59F200'}

lfi30_cosmoglobe = {'name':'/home/rcepeda/Desktop/data/cosmoglobe/processed/planck_030_1deg_nside512_CMBoff_KCMB.fits',
          'inst':'Planck',
          'frequency':28.4,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'KCMB',
          'bandpass':bandpasses.fastlficc,
          'nside':512,
          'fmt':'s',
          'CALERR':0.01,
          'color':'#59F200'}



lfi44 = {'name':'/home/rcepeda/Desktop/data/ancillary_data/CMBoff/LFI_SkyMap_44_512_smth.fits',
          'inst':'Planck',
          'frequency':44.1,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'KCMB',
          'bandpass':bandpasses.fastlficc,
          'nside':512,
          'fmt':'s',
          'CALERR':0.01,
          'color':'#59F200'}

lfi44_npipe = {'name':'/home/rcepeda/Desktop/data/npipe/processed/npipe6v20_044_1deg_nside512_CMBoff_KCMB.fits',
          'inst':'Planck',
          'frequency':44.1,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'KCMB',
          'bandpass':bandpasses.fastlficc,
          'nside':512,
          'fmt':'s',
          'CALERR':0.01,
          'color':'#59F200'}

lfi44_cosmoglobe = {'name':'/home/rcepeda/Desktop/data/cosmoglobe/processed/planck_044_1deg_nside512_CMBoff_KCMB.fits',
          'inst':'Planck',
          'frequency':44.1,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'KCMB',
          'bandpass':bandpasses.fastlficc,
          'nside':512,
          'fmt':'s',
          'CALERR':0.01,
          'color':'#59F200'}


lfi70 =  {'name':'/home/rcepeda/Desktop/data/ancillary_data/CMBoff/LFI_SkyMap_70_512_smth.fits',
          'inst':'Planck',
          'frequency':70.4,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'KCMB',
          'nside':512,
          'bandpass':bandpasses.fastlficc,
          'fmt':'s',
          'CALERR':0.01,
          'color':'#59F200'}

lfi70_npipe =  {'name':'/home/rcepeda/Desktop/data/npipe/processed/npipe6v20_070_1deg_nside512_CMBoff_KCMB.fits',
          'inst':'Planck',
          'frequency':70.4,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'KCMB',
          'nside':512,
          'bandpass':bandpasses.fastlficc,
          'fmt':'s',
          'CALERR':0.01,
          'color':'#59F200'}

lfi70_cosmoglobe =  {'name':'/home/rcepeda/Desktop/data/cosmoglobe/processed/planck_070_1deg_nside512_CMBoff_KCMB.fits',
          'inst':'Planck',
          'frequency':70.4,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'KCMB',
          'nside':512,
          'bandpass':bandpasses.fastlficc,
          'fmt':'s',
          'CALERR':0.01,
          'color':'#59F200'}


hfi100 = {'name':'/home/rcepeda/Desktop/data/ancillary_data/CMBoff/HFI_SkyMap_100_512_smth.fits',
          'inst':'Planck',
          'frequency':100.,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'KCMB',
          'nside':512,
          'fmt':'s',
          'color':'#59F200',
          'bandpass':bandpasses.fasthficc,
          'CALERR':0.01}

hfi100_npipe = {'name':'/home/rcepeda/Desktop/data/npipe/ricardo/planck_full_100ghz_corrco1_zls_dips_smth1deg_nside512.fits',
          'inst':'Planck',
          'frequency':100.,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'KCMB',
          'nside':512,
          'fmt':'s',
          'color':'#59F200',
          'bandpass':bandpasses.fasthficc,
          'CALERR':0.01}

hfi100_npipe_MJysr = {'name':'/home/rcepeda/Desktop/data/npipe/mjysr/planck_full_100ghz_corrco1_zls_dips_smth1deg_nside512_MJysr.fits',
          'inst':'Planck',
          'frequency':100.,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'MJysr',
          'nside':512,
          'fmt':'s',
          'color':'#59F200',
          'bandpass':bandpasses.fasthficc,
          'CALERR':0.01}


hfi143 = {'name':'/home/rcepeda/Desktop/data/ancillary_data/CMBoff/HFI_SkyMap_143_512_smth.fits',
          'inst':'Planck',
          'frequency':143.,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'KCMB',
          'nside':512,
          'fmt':'s',
          'color':'#59F200',
          'bandpass':bandpasses.fasthficc,
          'CALERR':0.01}

hfi143_npipe = {'name': '/home/rcepeda/Desktop/data/npipe/ricardo/planck_full_143ghz_zls_dips_smth1deg_nside512.fits',
          'inst':'Planck',
          'frequency':143.,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'KCMB',
          'nside':512,
          'fmt':'s',
          'color':'#59F200',
          'bandpass':bandpasses.fasthficc,
          'CALERR':0.01}

hfi143_npipe_MJysr = {'name': '/home/rcepeda/Desktop/data/npipe/mjysr/planck_full_143ghz_zls_dips_smth1deg_nside512_MJysr.fits',
          'inst':'Planck',
          'frequency':143.,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'MJysr',
          'nside':512,
          'fmt':'s',
          'color':'#59F200',
          'bandpass':bandpasses.fasthficc,
          'CALERR':0.01}


hfi217 = {'name':'/home/rcepeda/Desktop/data/ancillary_data/CMBoff/HFI_SkyMap_217_512_smth.fits',
          'inst':'Planck',
          'frequency':217.,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'KCMB',
          'nside':512,
          'fmt':'s',
          'color':'#59F200',
          'bandpass':bandpasses.fasthficc,
          'CALERR':0.01}

hfi217_npipe = {'name': '/home/rcepeda/Desktop/data/npipe/ricardo/planck_full_217ghz_corrco1_zls_dips_smth1deg_nside512.fits',
          'inst':'Planck',
          'frequency':217.,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'KCMB',
          'nside':512,
          'fmt':'s',
          'color':'#59F200',
          'bandpass':bandpasses.fasthficc,
          'CALERR':0.01}

hfi217_npipe_MJysr = {'name': '/home/rcepeda/Desktop/data/npipe/mjysr/planck_full_217ghz_corrco1_zls_dips_smth1deg_nside512_MJysr.fits',
          'inst':'Planck',
          'frequency':217.,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'MJysr',
          'nside':512,
          'fmt':'s',
          'color':'#59F200',
          'bandpass':bandpasses.fasthficc,
          'CALERR':0.01}


hfi353 = {'name':'/home/rcepeda/Desktop/data/ancillary_data/CMBoff/HFI_SkyMap_353_512_smth.fits',
          'inst':'Planck',
          'frequency':353.,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'KCMB',
          'nside':512,
          'fmt':'s',
          'color':'#59F200',
          'bandpass':bandpasses.fasthficc,
          'CALERR':0.013}

hfi353_npipe = {'name': '/home/rcepeda/Desktop/data/npipe/ricardo/planck_full_353ghz_corrco1_zls_dips_smth1deg_nside512.fits',
          'inst':'Planck',
          'frequency':353.,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'KCMB',
          'nside':512,
          'fmt':'s',
          'color':'#59F200',
          'bandpass':bandpasses.fasthficc,
          'CALERR':0.013}

hfi353_npipe_MJysr = {'name': '/home/rcepeda/Desktop/data/npipe/mjysr/planck_full_353ghz_corrco1_zls_dips_smth1deg_nside512_MJysr.fits',
          'inst':'Planck',
          'frequency':353.,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'MJysr',
          'nside':512,
          'fmt':'s',
          'color':'#59F200',
          'bandpass':bandpasses.fasthficc,
          'CALERR':0.013}


hfi545 = {'name':'/home/rcepeda/Desktop/data/ancillary_data/CMBon/HFI_SkyMap_545_512_smth.fits',
          'inst':'Planck',
          'frequency':545.,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'MJysr',
          'nside':512,
          'fmt':'s',
          'color':'#59F200',
          'bandpass':bandpasses.fasthficc,
          'CALERR':0.060}

hfi545_npipe = {'name':'/home/rcepeda/Desktop/data/npipe/ricardo/planck_full_545ghz_zls_dips_smth1deg_nside512.fits',
          'inst':'Planck',
          'frequency':545.,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'KCMB',
          'nside':512,
          'fmt':'s',
          'color':'#59F200',
          'bandpass':bandpasses.fasthficc,
          'CALERR':0.060}

hfi545_npipe_MJysr = {'name':'/home/rcepeda/Desktop/data/npipe/mjysr/planck_full_545ghz_zls_dips_smth1deg_nside512_MJysr.fits',
          'inst':'Planck',
          'frequency':545.,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'MJysr',
          'nside':512,
          'fmt':'s',
          'color':'#59F200',
          'bandpass':bandpasses.fasthficc,
          'CALERR':0.060}


hfi857 = {'name':'/home/rcepeda/Desktop/data/ancillary_data/CMBon/HFI_SkyMap_857_512_smth.fits',
          'inst':'Planck',
          'frequency':857.,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'MJysr',
          'nside':512,
          'fmt':'s',
          'color':'#59F200',
          'bandpass':bandpasses.fasthficc,
          'CALERR':0.064}

hfi857_npipe = {'name':'/home/rcepeda/Desktop/data/npipe/ricardo/planck_full_857ghz_zls_dips_smth1deg_nside512.fits',
          'inst':'Planck',
          'frequency':857.,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'KCMB',
          'nside':512,
          'fmt':'s',
          'color':'#59F200',
          'bandpass':bandpasses.fasthficc,
          'CALERR':0.064}

hfi857_npipe_MJysr = {'name':'/home/rcepeda/Desktop/data/npipe/mjysr/planck_full_857ghz_zls_dips_smth1deg_nside512_MJysr.fits',
          'inst':'Planck',
          'frequency':857.,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'MJysr',
          'nside':512,
          'fmt':'s',
          'color':'#59F200',
          'bandpass':bandpasses.fasthficc,
          'CALERR':0.064}


# DIRBE Maps

dirbe10= {'name':'/home/rcepeda/Desktop/data/ancillary_data/CMBon/DIRBE_ZSMA_10_256_smth.fits',
          'inst':'DIRBE',
          'frequency':1249.,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'MJysr',
          'nside':256,
          'fmt':'s',
          'color':'#ADADAD',
          'CALERR':0.135}


dirbe9 = {'name':'/home/rcepeda/Desktop/data/ancillary_data/CMBon/DIRBE_ZSMA_9_256_smth.fits',
          'inst':'DIRBE',
          'frequency':2141.,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'MJysr',
          'nside':256,
          'fmt':'s',
          'color':'#ADADAD',
          'CALERR':0.106}


dirbe8 = {'name':'/home/rcepeda/Desktop/data/ancillary_data/CMBon/DIRBE_ZSMA_8_256_smth.fits',
          'inst':'DIRBE',
          'frequency':2998.,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'MJysr',
          'nside':256,
          'fmt':'s',
          'color':'#ADADAD',
          'CALERR':0.116}


dirbe7 = {'name':'/home/rcepeda/Desktop/data/ancillary_data/CMBon/DIRBE_ZSMA_7_256_smth.fits',
          'inst':'DIRBE',
         'frequency':4997.,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'MJysr',
          'nside':256,
          'fmt':'s',
          'color':'#ADADAD',
          'CALERR':0.1}


dirbe6 = {'name':'/home/rcepeda/Desktop/data/ancillary_data/CMBon/DIRBE_ZSMA_6_256_smth.fits',
          'inst':'DIRBE',
          'frequency':11992.,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'MJysr',
          'nside':256,
          'fmt':'s',
          'color':'#ADADAD',
          'CALERR':0.1}



IRIS100 = {'name':'/home/rcepeda/Desktop/data/iris/IRIS_mollweide_nohole_4_512_smoothed.fits',
          'inst':'IRIS',
          'frequency':2998.,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'MJysr',
          'nside':512,
          'fmt':'s',
          'color':'#ADADAD',
          'CALERR':0.135}

IRIS60 = {'name':'/home/rcepeda/Desktop/data/iris/IRIS_mollweide_nohole_3_512_smoothed.fits',
          'inst':'IRIS',
          'frequency':4997.,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'MJysr',
          'nside':512,
          'fmt':'s',
          'color':'#ADADAD',
          'CALERR':0.104}

IRIS25 = {'name':'/home/rcepeda/Desktop/data/iris/IRIS_mollweide_nohole_2_512_smoothed.fits',
          'inst':'IRIS',
          'frequency':11992.,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'MJysr',
          'nside':512,
          'fmt':'s',
          'color':'#ADADAD',
          'CALERR':0.151}

IRIS12 = {'name':'/home/rcepeda/Desktop/data/iris/IRIS_mollweide_nohole_1_512_smoothed.fits',
          'inst':'IRIS',
          'frequency':24983.,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'MJysr',
          'nside':512,
          'fmt':'s',
          'color':'#ADADAD',
          'CALERR':0.051}



AKARI9_lambda_ori = {'name':'/home/rcepeda/Desktop/data/akari/akari_FWHM_1deg_NSIDE512.fits',
          'inst':'AKARI',
          'frequency': 33310.,
          'resolution':1.1331*(np.pi/180.)**2,
          'unit':'MJysr',
          'nside': 512,
          'fmt':'s',
          'color':'#ADADAD',
          'CALERR':0.1}
