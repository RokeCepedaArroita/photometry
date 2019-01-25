# List all the input files to be processed

import numpy as np
import bandpasses


## Config

'''
beam_eff_err accounts for the discrepancy between the beam-scale and large-scale calibration due to low beam efficiencies,
which affects the haslam, dwingeloo and reich maps resulting in an error of up to a factor of 2
'''

beam_eff_err = 0.4  # accounts for up to 40% beam efficiency error in a flux density measurement - only for haslam, dwingeloo and Reich



## Maps

# Low-Frequency (0.408-5 GHz) Maps

haslam = {'name':'/scratch/nas_falcon/scratch/rca/data/ancillary_data/CMBon/haslam408_ds_smth.fits',
          'inst':'HASLAM',
          'frequency':0.408,
          'resolution':1.13*(np.pi/180.)**2,
          'unit':'K',
          'nside':512,
          'fmt':'o',
          'color':'#F29900',
          'CALERR':(0.1**2+beam_eff_err**2)**0.5}

dwingeloo = {'name':'/scratch/nas_falcon/scratch/rca/data/ancillary_data/CMBon/dwingeloo_820.fits',
          'inst':'Dwingeloo',
          'frequency':0.820,
          'resolution':1.13*(np.pi/180.)**2,
          'unit':'K',
          'nside':128,
          'fmt':'o',
          'color':'#F29900',
          'CALERR':(0.1**2+beam_eff_err**2)**0.5}

Reich = {'name':'/scratch/nas_falcon/scratch/rca/data/ancillary_data/CMBon/512_60.00smoothed_reichlb21_1.42_512_1986.fits',
         'inst':'Reich',
         'frequency':1.42,
         'resolution':1.13*(np.pi/180.)**2,
         'unit':'mK',
         'nside':512,
         'fmt':'o',
         'color':'#31D63F',
         'CALERR':(0.05**2+beam_eff_err**2)**0.5}


Jonas = {'name':'/scratch/nas_falcon/scratch/rca/data/ancillary_data/others/512_60.00smoothed_jonas98_2.326_512_1998_K.fits',
         'inst':'Jonas',
         'frequency':2.326,
         'resolution':1.13*(np.pi/180.)**2,
         'unit':'K',
         'nside':512,
         'fmt':'o',
         'color':'#31D63F',
         'CALERR':0.05}


CBASS = {'name':'/scratch/nas_falcon/scratch/rca/data/ancillary_data/others/cbass_nighttime_512_smth.fits',
          'inst':'C-BASS',
          'frequency':4.76,
          'resolution':1.13*(np.pi/180.)**2,
          'unit':'K',
          'nside':512,
          'fmt':'o',
          'color':'#FDE5E5',
          'CALERR':0.05}




# QUIJOTE Maps


quijote11 = {'name':'/scratch/nas_falcon/scratch/rca/data/ancillary_data/CMBoff/calibrated_smth_11GHz.fits',
             'inst':'MFI',
             'frequency':11.,
             'resolution':1.13*(np.pi/180.)**2,
             'unit':'K',
             'nside':512,
             'bandpass':bandpasses.fastmficc,
             'fmt':'*',
             'color':'#9900F2',
             'CALERR':0.03}

quijote13 = {'name':'/scratch/nas_falcon/scratch/rca/data/ancillary_data/CMBoff/calibrated_smth_13GHz.fits',
              'inst':'MFI',
              'frequency':13.,
              'resolution':1.13*(np.pi/180.)**2,
              'unit':'K',
              'nside':512,
              'bandpass':bandpasses.fastmficc,
              'fmt':'*',
              'color':'#9900F2',
              'CALERR':0.03}

quijote17 = {'name':'/scratch/nas_falcon/scratch/rca/data/ancillary_data/CMBoff/calibrated_smth_17GHz.fits',
              'inst':'MFI',
              'frequency':17.,
              'resolution':1.13*(np.pi/180.)**2,
              'unit':'K',
              'nside':512,
              'bandpass':bandpasses.fastmficc,
              'fmt':'*',
              'color':'#9900F2',
              'CALERR':0.18}

quijote19 = {'name':'/scratch/nas_falcon/scratch/rca/data/ancillary_data/CMBoff/calibrated_smth_19GHz.fits',
             'inst':'MFI',
             'frequency':19.,
             'resolution':1.13*(np.pi/180.)**2,
             'unit':'K',
             'nside':512,
             'bandpass':bandpasses.fastmficc,
             'fmt':'*',
             'color':'#9900F2',
             'CALERR':0.28}


quijote11rhooph = {'name':'/scratch/nas_falcon/scratch/rca/data/ancillary_data/CMBon/CAL-RHOOPH-11GHz.fits',
             'inst':'MFI',
             'frequency':11.,
             'resolution':1.13*(np.pi/180.)**2,
             'unit':'K',
             'nside':512,
             'bandpass':bandpasses.fastmficc,
             'fmt':'*',
             'color':'#9900F2',
             'CALERR':0.10}

quijote13rhooph = {'name':'/scratch/nas_falcon/scratch/rca/data/ancillary_data/CMBon/CAL-RHOOPH-13GHz.fits',
              'inst':'MFI',
              'frequency':13.,
              'resolution':1.13*(np.pi/180.)**2,
              'unit':'K',
              'nside':512,
              'bandpass':bandpasses.fastmficc,
              'fmt':'*',
              'color':'#9900F2',
              'CALERR':0.10}


quijote17rhooph = {'name':'/scratch/nas_falcon/scratch/rca/data/ancillary_data/CMBon/UNCAL-RHOOPH-17GHz.fits',
             'inst':'MFI',
             'frequency':17.,
             'resolution':1.13*(np.pi/180.)**2,
             'unit':'K',
             'nside':512,
             'bandpass':bandpasses.fastmficc,
             'fmt':'*',
             'color':'#9900F2',
             'CALERR':0.1}

quijote19rhooph = {'name':'/scratch/nas_falcon/scratch/rca/data/ancillary_data/CMBon/UNCAL-RHOOPH-19GHz.fits',
              'inst':'MFI',
              'frequency':19.,
              'resolution':1.13*(np.pi/180.)**2,
              'unit':'K',
              'nside':512,
              'bandpass':bandpasses.fastmficc,
              'fmt':'*',
              'color':'#9900F2',
              'CALERR':0.1}




# WMAP and Planck


wmapK = {'name':'/scratch/nas_falcon/scratch/rca/data/ancillary_data/CMBoff/wmap_band_smth_imap_r9_9yr_K_v5.fits',
        'inst':'WMAP',
        'frequency':22.8,
        'resolution':1.13*(np.pi/180.)**2,
        'unit':'mKCMB',
        'nside':512,
        'fmt':'o',
        'bandpass':bandpasses.fastwmapcc,
        'CALERR':0.01,
        'color':'#0059F2'}

wmapKa= {'name':'/scratch/nas_falcon/scratch/rca/data/ancillary_data/CMBoff/wmap_band_smth_imap_r9_9yr_Ka_v5.fits',
         'inst':'WMAP',
         'frequency':33.,
         'resolution':1.13*(np.pi/180.)**2,
         'unit':'mKCMB',
         'nside':512,
         'fmt':'o',
         'bandpass':bandpasses.fastwmapcc,
         'CALERR':0.01,
         'color':'#0059F2'}

wmapQ = {'name':'/scratch/nas_falcon/scratch/rca/data/ancillary_data/CMBoff/wmap_band_smth_imap_r9_9yr_Q_v5.fits',
         'inst':'WMAP',
         'frequency':40.7,
         'resolution':1.13*(np.pi/180.)**2,
         'unit':'mKCMB',
         'nside':512,
         'fmt':'o',
         'bandpass':bandpasses.fastwmapcc,
         'CALERR':0.01,
         'color':'#0059F2'}

wmapV = {'name':'/scratch/nas_falcon/scratch/rca/data/ancillary_data/CMBoff/wmap_band_smth_imap_r9_9yr_V_v5.fits',
         'inst':'WMAP',
         'frequency':60.7,
         'resolution':1.13*(np.pi/180.)**2,
         'unit':'mKCMB',
         'nside':512,
         'fmt':'o',
         'bandpass':bandpasses.fastwmapcc,
         'CALERR':0.01,
         'color':'#0059F2'}

wmapW = {'name':'/scratch/nas_falcon/scratch/rca/data/ancillary_data/CMBoff/wmap_band_smth_imap_r9_9yr_W_v5.fits',
         'inst':'WMAP',
         'frequency':93.6,
         'resolution':1.13*(np.pi/180.)**2,
         'unit':'mKCMB',
         'nside':512,
         'fmt':'o',
         'bandpass':bandpasses.fastwmapcc,
         'CALERR':0.01,
         'color':'#0059F2'}


lfi30 = {'name':'/scratch/nas_falcon/scratch/rca/data/ancillary_data/CMBoff/LFI_SkyMap_30_512_smth.fits',
          'inst':'Planck',
          'frequency':28.4,
          'resolution':1.13*(np.pi/180.)**2,
          'unit':'KCMB',
          'bandpass':bandpasses.fastlficc,
          'nside':512,
          'fmt':'s',
          'CALERR':0.01,
          'color':'#59F200'}

lfi44 = {'name':'/scratch/nas_falcon/scratch/rca/data/ancillary_data/CMBoff/LFI_SkyMap_44_512_smth.fits',
          'inst':'Planck',
          'frequency':44.,
          'resolution':1.13*(np.pi/180.)**2,
          'unit':'KCMB',
          'bandpass':bandpasses.fastlficc,
          'nside':512,
          'fmt':'s',
          'CALERR':0.01,
          'color':'#59F200'}

lfi70 =  {'name':'/scratch/nas_falcon/scratch/rca/data/ancillary_data/CMBoff/LFI_SkyMap_70_512_smth.fits',
          'inst':'Planck',
          'frequency':70.,
          'resolution':1.13*(np.pi/180.)**2,
          'unit':'KCMB',
          'nside':512,
          'bandpass':bandpasses.fastlficc,
          'fmt':'s',
          'CALERR':0.01,
          'color':'#59F200'}

hfi100 = {'name':'//scratch/nas_falcon/scratch/rca/data/ancillary_data/CMBoff/HFI_SkyMap_100_512_smth.fits',
          'inst':'Planck',
          'frequency':100.,
          'resolution':1.13*(np.pi/180.)**2,
          'unit':'KCMB',
          'nside':512,
          'fmt':'s',
          'color':'#59F200',
          'bandpass':bandpasses.fasthficc,
          'CALERR':0.01}

hfi143 = {'name':'/scratch/nas_falcon/scratch/rca/data/ancillary_data/CMBoff/HFI_SkyMap_143_512_smth.fits',
          'inst':'Planck',
          'frequency':143.,
          'resolution':1.13*(np.pi/180.)**2,
          'unit':'KCMB',
          'nside':512,
          'fmt':'s',
          'color':'#59F200',
          'bandpass':bandpasses.fasthficc,
          'CALERR':0.01}

hfi217 = {'name':'/scratch/nas_falcon/scratch/rca/data/ancillary_data/CMBoff/HFI_SkyMap_217_512_smth.fits',
          'inst':'Planck',
          'frequency':217.,
          'resolution':1.13*(np.pi/180.)**2,
          'unit':'KCMB',
          'nside':512,
          'fmt':'s',
          'color':'#59F200',
          'bandpass':bandpasses.fasthficc,
          'CALERR':0.01}

hfi353 = {'name':'/scratch/nas_falcon/scratch/rca/data/ancillary_data/CMBoff/HFI_SkyMap_353_512_smth.fits',
          'inst':'Planck',
          'frequency':353.,
          'resolution':1.13*(np.pi/180.)**2,
          'unit':'KCMB',
          'nside':512,
          'fmt':'s',
          'color':'#59F200',
          'bandpass':bandpasses.fasthficc,
          'CALERR':0.013}

hfi545 = {'name':'/scratch/nas_falcon/scratch/rca/data/ancillary_data/CMBon/HFI_SkyMap_545_512_smth.fits',
          'inst':'Planck',
          'frequency':545.,
          'resolution':1.13*(np.pi/180.)**2,
          'unit':'MJysr',
          'nside':512,
          'fmt':'s',
          'color':'#59F200',
          'bandpass':bandpasses.fasthficc,
          'CALERR':0.013}

hfi857 = {'name':'/scratch/nas_falcon/scratch/rca/data/ancillary_data/CMBon/HFI_SkyMap_857_512_smth.fits',
          'inst':'Planck',
          'frequency':857.,
          'resolution':1.13*(np.pi/180.)**2,
          'unit':'MJysr',
          'nside':512,
          'fmt':'s',
          'color':'#59F200',
          'bandpass':bandpasses.fasthficc,
          'CALERR':0.014}




# DIRBE Maps

dirbe10= {'name':'/scratch/nas_falcon/scratch/rca/data/ancillary_data/CMBon/DIRBE_ZSMA_10_256_smth.fits',
          'inst':'DIRBE',
          'frequency':1249.,
          'resolution':1.13*(np.pi/180.)**2,
          'unit':'MJysr',
          'nside':256,
          'fmt':'s',
          'color':'#ADADAD',
          'CALERR':0.135}


dirbe9 = {'name':'/scratch/nas_falcon/scratch/rca/data/ancillary_data/CMBon/DIRBE_ZSMA_9_256_smth.fits',
          'inst':'DIRBE',
          'frequency':2141.,
          'resolution':1.13*(np.pi/180.)**2,
          'unit':'MJysr',
          'nside':256,
          'fmt':'s',
          'color':'#ADADAD',
          'CALERR':0.106}


dirbe8 = {'name':'/scratch/nas_falcon/scratch/rca/data/ancillary_data/CMBon/DIRBE_ZSMA_8_256_smth.fits',
          'inst':'DIRBE',
          'frequency':2998.,
          'resolution':1.13*(np.pi/180.)**2,
          'unit':'MJysr',
          'nside':256,
          'fmt':'s',
          'color':'#ADADAD',
          'CALERR':0.116}


dirbe7 = {'name':'/scratch/nas_falcon/scratch/rca/data/ancillary_data/CMBon/DIRBE_ZSMA_7_256_smth.fits',
         'frequency':4997.,
          'resolution':1.13*(np.pi/180.)**2,
          'unit':'MJysr',
          'nside':256,
          'fmt':'s',
          'color':'#ADADAD',
          'CALERR':0.1}


dirbe6 = {'name':'/scratch/nas_falcon/scratch/rca/data/ancillary_data/CMBon/DIRBE_ZSMA_6_256_smth.fits',
          'frequency':11992.,
          'resolution':1.13*(np.pi/180.)**2,
          'unit':'MJysr',
          'nside':256,
          'fmt':'s',
          'color':'#ADADAD',
          'CALERR':0.1}
