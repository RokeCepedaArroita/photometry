# Here is a collection of premade source dictionaries for known sources.
# All units in degrees, unless stated

'''
NOTE (TODO): the initial parameter guesses or fitting information are NOT used. This is something that will be done in the future.
Leave these as "None" for the time being since nothing is done with them. These settings are set in the mcmc_config file only.
'''


example ={'name':'source_name',

          # Source apertures
          'theta': [], # centre latitude position
          'phi': [],   # centre longitude position
          'ra': [],   # list of radii describing the major-axis of aperture
          'rb': [],   # list of minor-axes for elliptical apertures (can be False for circles)
          'pang':[],  # Rotation angles of ellipse
	      'frac':[],   # outer diameter divided by inner diameter

          # Background apertures
          'itheta': [], # List of background aperture latitudes
          'iphi': [],   # List of background aperture longitudes
          'ira':[],     # List of background aperture major-axes
          'irb':[],     # Background aperture minor-axes (false for cirles)
          'ipang':[],   # Rotation angles of ellipse
          'ifrac':[],     # Fractional interior radius (to make annulli/rings)
          'isweep':[],    # Angles to use for background annulli (False for 360 degrees) - sweep is clockwise

          # Initial Parameter guesses
          'sParams':{'A_ame':None,   # AME amplitude (unit)
                     'nu_mod':None, # AME centre frequency (GHz)
                     'EM':None ,   # Emission measure of free-free
                     'dT': None, # CMB fluctuation amplitude  (unit)
                     'Tdust': None, # Dust temperature amplitude (K)
                     'tau': None,   # Dust opacity
                     'beta':  None}, # Spectral index of modified dust BB

          # Fitting information
          'frange': None, # Frequency range (GHz)
          'FitErrs':None,
          'components':['sync', # Fit for synchrtron
                        'ff',   # ... free-free
                        'dust', # ... thermal dust
                        'cmb',  # ... cmb
                        'ame'], # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': None,
          'ame_file': None
          }



'''
UCHII PAPER SOURCES: these are PLanck AME sources flagged by Clive
Now we are using the AMI Galactic Plane Survey to study them
'''


S235 ={'name':'S235',

          # Source apertures
          'theta': [2.79],
          'phi': [173.62],
          'ra': [2.],
          'rb': [2.],
          'pang':[0.],
          'frac':[0.],

          # Background apertures
          'itheta': [2.79],
          'iphi': [173.62],
          'ira':[4.],
          'irb':[4.],
          'ipang':[0],
          'ifrac':[0.7],
          'isweep':[360.],

          # Initial Parameter guesses
          'sParams':{'A_ame':None,   # AME amplitude (unit)
                     'nu_mod':None, # AME centre frequency (GHz)
                     'EM':None ,   # Emission measure of free-free
                     'dT': None, # CMB fluctuation amplitude  (unit)
                     'Tdust': None, # Dust temperature amplitude (K)
                     'tau': None,   # Dust opacity
                     'beta': None}, # Spectral index of modified dust BB

          # Fitting information
          'frange': None, # Frequency range (GHz)
          'FitErrs':None,
          'components':None, # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': None,
          'ame_file': None
          }



W55 = {'name':'W55',

          # Source apertures
          'theta': [-0.21],
          'phi': [59.42],
          'ra': [1.],
          'rb': [1.],
          'pang':[0.],
          'frac':[0.],

          # Background apertures
          'itheta': [-0.21],
          'iphi': [59.42],
          'ira':[2.],
          'irb':[2.],
          'ipang':[0],
          'ifrac':[0.7],
          'isweep':[360.],

          # Initial Parameter guesses
          'sParams':{'A_ame':None,   # AME amplitude (unit)
                     'nu_mod':None, # AME centre frequency (GHz)
                     'EM':None ,   # Emission measure of free-free
                     'dT': None, # CMB fluctuation amplitude  (unit)
                     'Tdust': None, # Dust temperature amplitude (K)
                     'tau': None,   # Dust opacity
                     'beta': None}, # Spectral index of modified dust BB

          # Fitting information
          'frange': None, # Frequency range (GHz)
          'FitErrs':None,
          'components':None, # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': None,
          'ame_file': None
          }



RNeGM112 = {'name':'RNeGM1-12',

          # Source apertures
          'theta': [1.47],
          'phi': [98.00],
          'ra': [1.],
          'rb': [1.],
          'pang':[0.],
          'frac':[0.],

          # Background apertures
          'itheta': [1.47],
          'iphi': [98.00],
          'ira':[2.],
          'irb':[2.],
          'ipang':[0],
          'ifrac':[0.7],
          'isweep':[360.],

          # Initial Parameter guesses
          'sParams':{'A_ame':None,   # AME amplitude (unit)
                     'nu_mod':None, # AME centre frequency (GHz)
                     'EM':None ,   # Emission measure of free-free
                     'dT': None, # CMB fluctuation amplitude  (unit)
                     'Tdust': None, # Dust temperature amplitude (K)
                     'tau': None,   # Dust opacity
                     'beta': None}, # Spectral index of modified dust BB

          # Fitting information
          'frange': None, # Frequency range (GHz)
          'FitErrs':None,
          'components':None, # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': None,
          'ame_file': None
          }



DNeTGUH942 = {'name':'DNe-TGU-H942',

          # Source apertures
          'theta': [1.35],
          'phi': [142.35],
          'ra': [1.],
          'rb': [1.],
          'pang':[0.],
          'frac':[0.],

          # Background apertures
          'itheta': [1.35],
          'iphi': [142.35],
          'ira':[2.],
          'irb':[2.],
          'ipang':[0],
          'ifrac':[0.7],
          'isweep':[360.],

          # Initial Parameter guesses
          'sParams':{'A_ame':None,   # AME amplitude (unit)
                     'nu_mod':None, # AME centre frequency (GHz)
                     'EM':None ,   # Emission measure of free-free
                     'dT': None, # CMB fluctuation amplitude  (unit)
                     'Tdust': None, # Dust temperature amplitude (K)
                     'tau': None,   # Dust opacity
                     'beta': None}, # Spectral index of modified dust BB

          # Fitting information
          'frange': None, # Frequency range (GHz)
          'FitErrs':None,
          'components':None, # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': None,
          'ame_file': None
          }



NGC2174 = {'name':'NGC2174',

          # Source apertures
          'theta': [0.46],
          'phi': [190.00],
          'ra': [1.],
          'rb': [1.],
          'pang':[0.],
          'frac':[0.],

          # Background apertures
          'itheta': [0.46],
          'iphi': [190.00],
          'ira':[2.],
          'irb':[2.],
          'ipang':[0],
          'ifrac':[0.7],
          'isweep':[360.],

          # Initial Parameter guesses
          'sParams':{'A_ame':None,   # AME amplitude (unit)
                     'nu_mod':None, # AME centre frequency (GHz)
                     'EM':None ,   # Emission measure of free-free
                     'dT': None, # CMB fluctuation amplitude  (unit)
                     'Tdust': None, # Dust temperature amplitude (K)
                     'tau': None,   # Dust opacity
                     'beta': None}, # Spectral index of modified dust BB

          # Fitting information
          'frange': None, # Frequency range (GHz)
          'FitErrs':None,
          'components':None, # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': None,
          'ame_file': None
          }


california_nebula ={'name':'California',

          # Source apertures
          'theta': [-12.05],
          'phi': [160.60],
          'ra': [2.],
          'rb': [2.],
          'pang':[-80.],
          'frac':[0.],

          # Background apertures
          'itheta': [-12.05],
          'iphi': [160.60],
          'ira':[3.5],
          'irb':[3.5],
          'ipang':[-80.],
          'ifrac':[0.75],
          'isweep':[360.],

          # Initial Parameter guesses
          'sParams':{'A_ame':None,   # AME amplitude (unit)
                     'nu_mod':None, # AME centre frequency (GHz)
                     'EM':None ,   # Emission measure of free-free
                     'dT': None, # CMB fluctuation amplitude  (unit)
                     'Tdust': None, # Dust temperature amplitude (K)
                     'tau': None,   # Dust opacity
                     'beta': None}, # Spectral index of modified dust BB

          # Fitting information
          'frange': None, # Frequency range (GHz)
          'FitErrs':None,
          'components':None, # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': None,
          'ame_file': None
          }



SH288 = {'name':'SH2-88',

          # Source apertures
          'theta': [0.11],
          'phi': [61.47],
          'ra': [1.],
          'rb': [1.],
          'pang':[0.],
          'frac':[0.],

          # Background apertures
          'itheta': [0.11],
          'iphi': [61.47],
          'ira':[2.],
          'irb':[2.],
          'ipang':[0],
          'ifrac':[0.7],
          'isweep':[360.],

          # Initial Parameter guesses
          'sParams':{'A_ame':None,   # AME amplitude (unit)
                     'nu_mod':None, # AME centre frequency (GHz)
                     'EM':None ,   # Emission measure of free-free
                     'dT': None, # CMB fluctuation amplitude  (unit)
                     'Tdust': None, # Dust temperature amplitude (K)
                     'tau': None,   # Dust opacity
                     'beta': None}, # Spectral index of modified dust BB

          # Fitting information
          'frange': None, # Frequency range (GHz)
          'FitErrs':None,
          'components':None, # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': None,
          'ame_file': None
          }


S89 = {'name':'S89',

          # Source apertures
          'theta': [0.05],
          'phi': [62.98],
          'ra': [1.],
          'rb': [1.],
          'pang':[0.],
          'frac':[0.],

          # Background apertures
          'itheta': [0.05],
          'iphi': [62.98],
          'ira':[2.],
          'irb':[2.],
          'ipang':[0],
          'ifrac':[0.7],
          'isweep':[360.],

          # Initial Parameter guesses
          'sParams':{'A_ame':None,   # AME amplitude (unit)
                     'nu_mod':None, # AME centre frequency (GHz)
                     'EM':None ,   # Emission measure of free-free
                     'dT': None, # CMB fluctuation amplitude  (unit)
                     'Tdust': None, # Dust temperature amplitude (K)
                     'tau': None,   # Dust opacity
                     'beta': None}, # Spectral index of modified dust BB

          # Fitting information
          'frange': None, # Frequency range (GHz)
          'FitErrs':None,
          'components':None, # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': None,
          'ame_file': None
          }


S98 = {'name':'S98',

          # Source apertures
          'theta': [1.02],
          'phi': [68.16],
          'ra': [1.],
          'rb': [1.],
          'pang':[0.],
          'frac':[0.],

          # Background apertures
          'itheta': [1.02],
          'iphi': [68.16],
          'ira':[2.],
          'irb':[2.],
          'ipang':[0],
          'ifrac':[0.7],
          'isweep':[360.],

          # Initial Parameter guesses
          'sParams':{'A_ame':None,   # AME amplitude (unit)
                     'nu_mod':None, # AME centre frequency (GHz)
                     'EM':None ,   # Emission measure of free-free
                     'dT': None, # CMB fluctuation amplitude  (unit)
                     'Tdust': None, # Dust temperature amplitude (K)
                     'tau': None,   # Dust opacity
                     'beta': None}, # Spectral index of modified dust BB

          # Fitting information
          'frange': None, # Frequency range (GHz)
          'FitErrs':None,
          'components':None, # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': None,
          'ame_file': None
          }



S101 = {'name':'S101',

          # Source apertures
          'theta': [2.85],
          'phi': [71.59],
          'ra': [1.],
          'rb': [1.],
          'pang':[0.],
          'frac':[0.],

          # Background apertures
          'itheta': [2.85],
          'iphi': [71.59],
          'ira':[2.],
          'irb':[2.],
          'ipang':[0],
          'ifrac':[0.7],
          'isweep':[360.],

          # Initial Parameter guesses
          'sParams':{'A_ame':None,   # AME amplitude (unit)
                     'nu_mod':None, # AME centre frequency (GHz)
                     'EM':None ,   # Emission measure of free-free
                     'dT': None, # CMB fluctuation amplitude  (unit)
                     'Tdust': None, # Dust temperature amplitude (K)
                     'tau': None,   # Dust opacity
                     'beta': None}, # Spectral index of modified dust BB

          # Fitting information
          'frange': None, # Frequency range (GHz)
          'FitErrs':None,
          'components':None, # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': None,
          'ame_file': None
          }


SH2105 = {'name':'SH2-105',

          # Source apertures
          'theta': [0.39],
          'phi': [75.81],
          'ra': [1.],
          'rb': [1.],
          'pang':[0.],
          'frac':[0.],

          # Background apertures
          'itheta': [0.39],
          'iphi': [75.81],
          'ira':[2.],
          'irb':[2.],
          'ipang':[0],
          'ifrac':[0.7],
          'isweep':[360.],

          # Initial Parameter guesses
          'sParams':{'A_ame':None,   # AME amplitude (unit)
                     'nu_mod':None, # AME centre frequency (GHz)
                     'EM':None ,   # Emission measure of free-free
                     'dT': None, # CMB fluctuation amplitude  (unit)
                     'Tdust': None, # Dust temperature amplitude (K)
                     'tau': None,   # Dust opacity
                     'beta': None}, # Spectral index of modified dust BB

          # Fitting information
          'frange': None, # Frequency range (GHz)
          'FitErrs':None,
          'components':None, # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': None,
          'ame_file': None
          }



S106 = {'name':'S106',

          # Source apertures
          'theta': [-0.62],
          'phi': [76.38],
          'ra': [1.],
          'rb': [1.],
          'pang':[0.],
          'frac':[0.],

          # Background apertures
          'itheta': [-0.62],
          'iphi': [76.38],
          'ira':[2.],
          'irb':[2.],
          'ipang':[0],
          'ifrac':[0.7],
          'isweep':[360.],

          # Initial Parameter guesses
          'sParams':{'A_ame':None,   # AME amplitude (unit)
                     'nu_mod':None, # AME centre frequency (GHz)
                     'EM':None ,   # Emission measure of free-free
                     'dT': None, # CMB fluctuation amplitude  (unit)
                     'Tdust': None, # Dust temperature amplitude (K)
                     'tau': None,   # Dust opacity
                     'beta': None}, # Spectral index of modified dust BB

          # Fitting information
          'frange': None, # Frequency range (GHz)
          'FitErrs':None,
          'components':None, # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': None,
          'ame_file': None
          }



HIIDR23 = {'name':'HII-DR23',

          # Source apertures
          'theta': [0.01],
          'phi': [81.59],
          'ra': [1.],
          'rb': [1.],
          'pang':[0.],
          'frac':[0.],

          # Background apertures
          'itheta': [0.01],
          'iphi': [81.59],
          'ira':[2.],
          'irb':[2.],
          'ipang':[0],
          'ifrac':[0.7],
          'isweep':[360.],

          # Initial Parameter guesses
          'sParams':{'A_ame':None,   # AME amplitude (unit)
                     'nu_mod':None, # AME centre frequency (GHz)
                     'EM':None ,   # Emission measure of free-free
                     'dT': None, # CMB fluctuation amplitude  (unit)
                     'Tdust': None, # Dust temperature amplitude (K)
                     'tau': None,   # Dust opacity
                     'beta': None}, # Spectral index of modified dust BB

          # Fitting information
          'frange': None, # Frequency range (GHz)
          'FitErrs':None,
          'components':None, # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': None,
          'ame_file': None
          }



HIIGAL09306281 = {'name':'HII-GAL093.06+2.81',

          # Source apertures
          'theta': [2.76],
          'phi': [93.02],
          'ra': [1.],
          'rb': [1.],
          'pang':[0.],
          'frac':[0.],

          # Background apertures
          'itheta': [2.76],
          'iphi': [93.02],
          'ira':[2.],
          'irb':[2.],
          'ipang':[0],
          'ifrac':[0.7],
          'isweep':[360.],

          # Initial Parameter guesses
          'sParams':{'A_ame':None,   # AME amplitude (unit)
                     'nu_mod':None, # AME centre frequency (GHz)
                     'EM':None ,   # Emission measure of free-free
                     'dT': None, # CMB fluctuation amplitude  (unit)
                     'Tdust': None, # Dust temperature amplitude (K)
                     'tau': None,   # Dust opacity
                     'beta': None}, # Spectral index of modified dust BB

          # Fitting information
          'frange': None, # Frequency range (GHz)
          'FitErrs':None,
          'components':None, # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': None,
          'ame_file': None
          }


LDN1059 = {'name':'LDN1059',

          # Source apertures
          'theta': [-1.53],
          'phi': [94.47],
          'ra': [1.],
          'rb': [1.],
          'pang':[0.],
          'frac':[0.],

          # Background apertures
          'itheta': [-1.53],
          'iphi': [94.47],
          'ira':[2.],
          'irb':[2.],
          'ipang':[0],
          'ifrac':[0.7],
          'isweep':[360.],

          # Initial Parameter guesses
          'sParams':{'A_ame':None,   # AME amplitude (unit)
                     'nu_mod':None, # AME centre frequency (GHz)
                     'EM':None ,   # Emission measure of free-free
                     'dT': None, # CMB fluctuation amplitude  (unit)
                     'Tdust': None, # Dust temperature amplitude (K)
                     'tau': None,   # Dust opacity
                     'beta': None}, # Spectral index of modified dust BB

          # Fitting information
          'frange': None, # Frequency range (GHz)
          'FitErrs':None,
          'components':None, # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': None,
          'ame_file': None
          }


TR37 = {'name':'TR37',

          # Source apertures
          'theta': [3.70],
          'phi': [99.60],
          'ra': [1.],
          'rb': [1.],
          'pang':[0.],
          'frac':[0.],

          # Background apertures
          'itheta': [3.70],
          'iphi': [99.60],
          'ira':[2.],
          'irb':[2.],
          'ipang':[0],
          'ifrac':[0.7],
          'isweep':[360.],

          # Initial Parameter guesses
          'sParams':{'A_ame':None,   # AME amplitude (unit)
                     'nu_mod':None, # AME centre frequency (GHz)
                     'EM':None ,   # Emission measure of free-free
                     'dT': None, # CMB fluctuation amplitude  (unit)
                     'Tdust': None, # Dust temperature amplitude (K)
                     'tau': None,   # Dust opacity
                     'beta': None}, # Spectral index of modified dust BB

          # Fitting information
          'frange': None, # Frequency range (GHz)
          'FitErrs':None,
          'components':None, # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': None,
          'ame_file': None
          }



LDN1161 = {'name':'LDN1161',

          # Source apertures
          'theta': [-0.69],
          'phi': [102.88],
          'ra': [1.],
          'rb': [1.],
          'pang':[0.],
          'frac':[0.],

          # Background apertures
          'itheta': [-0.69],
          'iphi': [102.88],
          'ira':[2.],
          'irb':[2.],
          'ipang':[0],
          'ifrac':[0.7],
          'isweep':[360.],

          # Initial Parameter guesses
          'sParams':{'A_ame':None,   # AME amplitude (unit)
                     'nu_mod':None, # AME centre frequency (GHz)
                     'EM':None ,   # Emission measure of free-free
                     'dT': None, # CMB fluctuation amplitude  (unit)
                     'Tdust': None, # Dust temperature amplitude (K)
                     'tau': None,   # Dust opacity
                     'beta': None}, # Spectral index of modified dust BB

          # Fitting information
          'frange': None, # Frequency range (GHz)
          'FitErrs':None,
          'components':None, # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': None,
          'ame_file': None
          }



DNeTGUH684 = {'name':'DNe-TGU-H684',

          # Source apertures
          'theta': [0.00],
          'phi': [109.01],
          'ra': [1.],
          'rb': [1.],
          'pang':[0.],
          'frac':[0.],

          # Background apertures
          'itheta': [0.00],
          'iphi': [109.01],
          'ira':[2.],
          'irb':[2.],
          'ipang':[0],
          'ifrac':[0.7],
          'isweep':[360.],

          # Initial Parameter guesses
          'sParams':{'A_ame':None,   # AME amplitude (unit)
                     'nu_mod':None, # AME centre frequency (GHz)
                     'EM':None ,   # Emission measure of free-free
                     'dT': None, # CMB fluctuation amplitude  (unit)
                     'Tdust': None, # Dust temperature amplitude (K)
                     'tau': None,   # Dust opacity
                     'beta': None}, # Spectral index of modified dust BB

          # Fitting information
          'frange': None, # Frequency range (GHz)
          'FitErrs':None,
          'components':None, # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': None,
          'ame_file': None
          }


HIIGAL1102025 = {'name':'HII-GAL110.2+02.5',

          # Source apertures
          'theta': [2.58],
          'phi': [110.25],
          'ra': [1.],
          'rb': [1.],
          'pang':[0.],
          'frac':[0.],

          # Background apertures
          'itheta': [2.58],
          'iphi': [110.25],
          'ira':[2.],
          'irb':[2.],
          'ipang':[0],
          'ifrac':[0.7],
          'isweep':[360.],

          # Initial Parameter guesses
          'sParams':{'A_ame':None,   # AME amplitude (unit)
                     'nu_mod':None, # AME centre frequency (GHz)
                     'EM':None ,   # Emission measure of free-free
                     'dT': None, # CMB fluctuation amplitude  (unit)
                     'Tdust': None, # Dust temperature amplitude (K)
                     'tau': None,   # Dust opacity
                     'beta': None}, # Spectral index of modified dust BB

          # Fitting information
          'frange': None, # Frequency range (GHz)
          'FitErrs':None,
          'components':None, # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': None,
          'ame_file': None
          }


W3 = {'name':'W3',

          # Source apertures
          'theta': [1.22],
          'phi': [133.74],
          'ra': [1.],
          'rb': [1.],
          'pang':[0.],
          'frac':[0.],

          # Background apertures
          'itheta': [1.22],
          'iphi': [133.74],
          'ira':[2.],
          'irb':[2.],
          'ipang':[0],
          'ifrac':[0.7],
          'isweep':[360.],

          # Initial Parameter guesses
          'sParams':{'A_ame':None,   # AME amplitude (unit)
                     'nu_mod':None, # AME centre frequency (GHz)
                     'EM':None ,   # Emission measure of free-free
                     'dT': None, # CMB fluctuation amplitude  (unit)
                     'Tdust': None, # Dust temperature amplitude (K)
                     'tau': None,   # Dust opacity
                     'beta': None}, # Spectral index of modified dust BB

          # Fitting information
          'frange': None, # Frequency range (GHz)
          'FitErrs':None,
          'components':None, # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': None,
          'ame_file': None
          }




SH2209 = {'name':'SH2-209',

          # Source apertures
          'theta': [-0.28],
          'phi': [151.62],
          'ra': [1.],
          'rb': [1.],
          'pang':[0.],
          'frac':[0.],

          # Background apertures
          'itheta': [-0.28],
          'iphi': [151.62],
          'ira':[2.],
          'irb':[2.],
          'ipang':[0],
          'ifrac':[0.7],
          'isweep':[360.],

          # Initial Parameter guesses
          'sParams':{'A_ame':None,   # AME amplitude (unit)
                     'nu_mod':None, # AME centre frequency (GHz)
                     'EM':None ,   # Emission measure of free-free
                     'dT': None, # CMB fluctuation amplitude  (unit)
                     'Tdust': None, # Dust temperature amplitude (K)
                     'tau': None,   # Dust opacity
                     'beta': None}, # Spectral index of modified dust BB

          # Fitting information
          'frange': None, # Frequency range (GHz)
          'FitErrs':None,
          'components':None, # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': None,
          'ame_file': None
          }



NGC1893 = {'name':'NGC1893',

          # Source apertures
          'theta': [-1.76],
          'phi': [173.56],
          'ra': [1.],
          'rb': [1.],
          'pang':[0.],
          'frac':[0.],

          # Background apertures
          'itheta': [-1.76],
          'iphi': [173.56],
          'ira':[2.],
          'irb':[2.],
          'ipang':[0],
          'ifrac':[0.7],
          'isweep':[360.],

          # Initial Parameter guesses
          'sParams':{'A_ame':None,   # AME amplitude (unit)
                     'nu_mod':None, # AME centre frequency (GHz)
                     'EM':None ,   # Emission measure of free-free
                     'dT': None, # CMB fluctuation amplitude  (unit)
                     'Tdust': None, # Dust temperature amplitude (K)
                     'tau': None,   # Dust opacity
                     'beta': None}, # Spectral index of modified dust BB

          # Fitting information
          'frange': None, # Frequency range (GHz)
          'FitErrs':None,
          'components':None, # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': None,
          'ame_file': None
          }



LDN1557 = {'name':'LDN1557',

          # Source apertures
          'theta': [4.30],
          'phi': [180.80],
          'ra': [1.],
          'rb': [1.],
          'pang':[0.],
          'frac':[0.],

          # Background apertures
          'itheta': [4.30],
          'iphi': [180.80],
          'ira':[2.],
          'irb':[2.],
          'ipang':[0],
          'ifrac':[0.7],
          'isweep':[360.],

          # Initial Parameter guesses
          'sParams':{'A_ame':None,   # AME amplitude (unit)
                     'nu_mod':None, # AME centre frequency (GHz)
                     'EM':None ,   # Emission measure of free-free
                     'dT': None, # CMB fluctuation amplitude  (unit)
                     'Tdust': None, # Dust temperature amplitude (K)
                     'tau': None,   # Dust opacity
                     'beta': None}, # Spectral index of modified dust BB

          # Fitting information
          'frange': None, # Frequency range (GHz)
          'FitErrs':None,
          'components':None, # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': None,
          'ame_file': None
          }




HIILBN182300007 = {'name':'HII-LBN182.30+00.07',

          # Source apertures
          'theta': [0.22],
          'phi': [182.36],
          'ra': [1.],
          'rb': [1.],
          'pang':[0.],
          'frac':[0.],

          # Background apertures
          'itheta': [0.22],
          'iphi': [182.36],
          'ira':[2.],
          'irb':[2.],
          'ipang':[-30.],
          'ifrac':[0.7],
          'isweep':[90.],

          # Initial Parameter guesses
          'sParams':{'A_ame':None,   # AME amplitude (unit)
                     'nu_mod':None, # AME centre frequency (GHz)
                     'EM':None ,   # Emission measure of free-free
                     'dT': None, # CMB fluctuation amplitude  (unit)
                     'Tdust': None, # Dust temperature amplitude (K)
                     'tau': None,   # Dust opacity
                     'beta': None}, # Spectral index of modified dust BB

          # Fitting information
          'frange': None, # Frequency range (GHz)
          'FitErrs':None,
          'components':None, # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': None,
          'ame_file': None
          }






'''
OLD SOURCES: pre-February 2019. Most of these are Roke's but there are
some relics from Stuat's PhD!
'''


ldn1622 ={'name':'LDN1622',

          # Source apertures
          'theta': [-11.65],
          'phi': [204.5],
          'ra': [1.],
          'rb': [2.],
          'pang':[30.],
          'frac':[0.],

          # Background apertures
          'itheta': [-11.65],
          'iphi': [204.5],
          'ira':[2.],
          'irb':[4.],
          'ipang':[30.],
          'ifrac':[0.5],
          'isweep':[360.],

          # Initial Parameter guesses
          'sParams':{'A_ame':1,   # AME amplitude (unit)
                     'nu_mod':30, # AME centre frequency (GHz)
                     'EM':200 ,   # Emission measure of free-free
                     'dT': 26.91e-6, # CMB fluctuation amplitude  (unit)
                     'Tdust': 17.06, # Dust temperature amplitude (K)
                     'tau': -3.09,   # Dust opacity
                     'beta':  2.14}, # Spectral index of modified dust BB

          # Fitting information
          'frange':[0.,10000.], # Frequency range (GHz)
          'FitErrs':[],
          'components':['sync', # Fit for synchrtron
                        'ff',   # ... free-free
                        'dust', # ... thermal dust
                        'ame'], # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': 'LDN1622Fluxes.npy',
          'ame_file': 'MC.dat'
          }


taua ={'name':'TauA',

          # Source apertures
          'theta': [-5.7844],
          'phi': [184.5575],
          'ra': [2.],
          'rb': [2.],
          'pang':[30.],
          'frac':[0.],

          # Background apertures
          'itheta': [-5.7844],
          'iphi': [184.5575],
          'ira':[4.25],
          'irb':[4.25],
          'ipang':[-270.],
          'ifrac':[0.7],
          'isweep':[180.],

          # Initial Parameter guesses
          'sParams':{'A_ame':1,   # AME amplitude (unit)
                     'nu_mod':30, # AME centre frequency (GHz)
                     'EM':200 ,   # Emission measure of free-free
                     'dT': 26.91e-6, # CMB fluctuation amplitude  (unit)
                     'Tdust': 17.06, # Dust temperature amplitude (K)
                     'tau': -3.09,   # Dust opacity
                     'beta':  2.14}, # Spectral index of modified dust BB

          # Fitting information
          'frange':[0.,10000.], # Frequency range (GHz)
          'FitErrs':[],
          'components':['sync','dust'], # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': 'TauAFluxes.npy',
          'ame_file': None
          }

casa ={'name':'CasA',

          # Source apertures
          'theta': [-2.1296],
          'phi': [111.7347],
          'ra': [2.],
          'rb': [2.],
          'pang':[30.],
          'frac':[0],

          # Background apertures
          'itheta': [-2.1296],
          'iphi': [111.7347],
          'ira':[4.25],
          'irb':[4.25],
          'ipang':[-270.],
          'ifrac':[0.7],
          'isweep':[180.],

          # Initial Parameter guesses
          'sParams':{'A_ame':1,   # AME amplitude (unit)
                     'nu_mod':30, # AME centre frequency (GHz)
                     'EM':200 ,   # Emission measure of free-free
                     'dT': 26.91e-6, # CMB fluctuation amplitude  (unit)
                     'Tdust': 17.06, # Dust temperature amplitude (K)
                     'tau': -3.09,   # Dust opacity
                     'beta':  2.14}, # Spectral index of modified dust BB

          # Fitting information
          'frange':[0.,10000.], # Frequency range (GHz)
          'FitErrs':[],
          'components':['sync','dust'], # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': 'CasAFluxes.npy',
          'ame_file': None
          }


cyga ={'name':'CygA',

          # Source apertures
          'theta': [05.7554],
          'phi': [76.1899],
          'ra': [2.],
          'rb': [2.],
          'pang':[30.],
          'frac':[0],

          # Background apertures
          'itheta': [05.7554],
          'iphi': [76.1899],
          'ira':[4.25],
          'irb':[4.25],
          'ipang':[-60.],
          'ifrac':[0.7],
          'isweep':[180.],

          # Initial Parameter guesses
          'sParams':{'A_ame':1,   # AME amplitude (unit)
                     'nu_mod':30, # AME centre frequency (GHz)
                     'EM':200 ,   # Emission measure of free-free
                     'dT': 26.91e-6, # CMB fluctuation amplitude  (unit)
                     'Tdust': 17.06, # Dust temperature amplitude (K)
                     'tau': -3.09,   # Dust opacity
                     'beta':  2.14}, # Spectral index of modified dust BB

          # Fitting information
          'frange':[0.,10000.], # Frequency range (GHz)
          'FitErrs':[],
          'components':['sync','dust'], # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': 'CygAFluxes.npy',
          'ame_file': None
          }


vira ={'name':'VirA',

          # Source apertures
          'theta': [74.4912],
          'phi': [283.7777],
          'ra': [2.],
          'rb': [2.*3.],
          'pang':[0.],
          'frac':[0],

          # Background apertures
          'itheta': [74.4912],
          'iphi': [283.7777],
          'ira':[4.25],
          'irb':[4.25*3.],
          'ipang':[0.],
          'ifrac':[0.7],
          'isweep':[360.],

          # Initial Parameter guesses
          'sParams':{'A_ame':1,   # AME amplitude (unit)
                     'nu_mod':30, # AME centre frequency (GHz)
                     'EM':200 ,   # Emission measure of free-free
                     'dT': 26.91e-6, # CMB fluctuation amplitude  (unit)
                     'Tdust': 17.06, # Dust temperature amplitude (K)
                     'tau': -3.09,   # Dust opacity
                     'beta':  2.14}, # Spectral index of modified dust BB

          # Fitting information
          'frange':[0.,10000.], # Frequency range (GHz)
          'FitErrs':[],
          'components':['sync','dust'], # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': 'VirAFLuxes.npy',
          'ame_file': None
          }




california ={'name':'California',

          # Source apertures
          'theta': [-12.36],
          'phi': [160.2],
          'ra': [2.5],
          'rb': [1.],
          'pang':[-80.],
          'frac':[0.],

          # Background apertures
          'itheta': [-12.36],
          'iphi': [160.2],
          'ira':[4.],
          'irb':[2.],
          'ipang':[-80.],
          'ifrac':[0.75],
          'isweep':[360.],

          # Initial Parameter guesses
          'sParams':{'A_ame':1,   # AME amplitude (unit)
                     'nu_mod':30, # AME centre frequency (GHz)
                     'EM':200 ,   # Emission measure of free-free
                     'dT': 26.91e-6, # CMB fluctuation amplitude  (unit)
                     'Tdust': 17.06, # Dust temperature amplitude (K)
                     'tau': -3.09,   # Dust opacity
                     'beta':  2.14}, # Spectral index of modified dust BB

          # Fitting information
          'frange':[0.,10000.], # Frequency range (GHz)
          'FitErrs':[],
          'components':['ff','dust'], # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': 'CaliforniaFlux.npy'   ,
          'ame_file': None
          }


californiaame ={'name':'California_AME',

          # Source apertures
          'theta': [-12.36],
          'phi': [160.2],
          'ra': [2.5],
          'rb': [1.],
          'pang':[-80.],
	  'frac':[0.],

          # Background apertures
          'itheta': [-12.36],
          'iphi': [160.2],
          'ira':[4.],
          'irb':[2.],
          'ipang':[-80.-180.],
          'ifrac':[0.75],
          'isweep':[100.],

          # Initial Parameter guesses
          'sParams':{'A_ame':1,   # AME amplitude (unit)
                     'nu_mod':30, # AME centre frequency (GHz)
                     'EM':200 ,   # Emission measure of free-free
                     'dT': 26.91e-6, # CMB fluctuation amplitude  (unit)
                     'Tdust': 17.06, # Dust temperature amplitude (K)
                     'tau': -3.09,   # Dust opacity
                     'beta':  2.14}, # Spectral index of modified dust BB

          # Fitting information
          'frange':[0.,10000.], # Frequency range (GHz)
          'FitErrs':[],
          'components':['ff','dust'], # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': 'CaliforniaFlux.npy'   ,
          'ame_file': 'MC.dat'
          }


rhooph ={'name':'Rho-Oph',

          # Source apertures
          'theta': [16.9],
          'phi': [-6.95],
          'ra': [2.0/2.0],
          'rb': [2.0/2.0],
          'pang':[-80.],
          'frac':[0.],

          # Background apertures
          'itheta': [16.9],
          'iphi': [-6.95],
          'ira':[4./2.0],
          'irb':[4./2.0],
          'ipang':[-180.],
          'ifrac':[0.675],
          'isweep':[180.],

          # Initial Parameter guesses
          'sParams':{'A_ame':1,   # AME amplitude (unit)
                     'nu_mod':30, # AME centre frequency (GHz)
                     'EM':200 ,   # Emission measure of free-free
                     'dT': 26.91e-6, # CMB fluctuation amplitude  (unit)
                     'Tdust': 17.06, # Dust temperature amplitude (K)
                     'tau': -3.09,   # Dust opacity
                     'beta':  2.14}, # Spectral index of modified dust BB

          # Fitting information
          'frange':[0.,10000.], # Frequency range (GHz)
          'FitErrs':[],
          'components':['ame','ff','dust','cmb'], # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': 'RhoOphFlux.npy'   ,
          'ame_file': 'WNM.dat'
          }



perseus ={'name':'Perseus',

          # Source apertures
          'theta': [-18.62],
          'phi': [160.26],
          'ra': [1.6],
          'rb': [1.0],
          'pang':[-51.],
          'frac':[0.],

          # Background apertures
          'itheta': [-18.62],
          'iphi': [160.26],
          'ira':[2.4*1.3],
          'irb':[1.5*1.3],
          'ipang':[-51.],
          'ifrac':[0.7],
          'isweep':[360.],

          # Initial Parameter guesses
          'sParams':{'A_ame':1,   # AME amplitude (unit)
                     'nu_mod':30, # AME centre frequency (GHz)
                     'EM':200 ,   # Emission measure of free-free
                     'dT': 26.91e-6, # CMB fluctuation amplitude  (unit)
                     'Tdust': 17.06, # Dust temperature amplitude (K)
                     'tau': -3.09,   # Dust opacity
                     'beta':  2.14}, # Spectral index of modified dust BB

          # Fitting information
          'frange':[0.,10000.], # Frequency range (GHz)
          'FitErrs':[],
          'components':[ # Fit for synchrtron
                        'ff',   # ... free-free
                        'dust', # ... thermal dust
                        'ame'], # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': 'PerseusFlux.npy'   ,
          'ame_file': 'MC.dat'
          }



perseus2 ={'name':'Perseus2',

          # Source apertures
          'theta': [-18.62],
          'phi': [160.26],
          'ra': [2.56],
          'rb': [1.6],
          'pang':[-51.],
          'frac':[0.],

          # Background apertures
          'itheta': [-18.62],
          'iphi': [160.26],
          'ira':[5.76],
          'irb':[3.6],
          'ipang':[-51.],
          'ifrac':[0.6],
          'isweep':[360.],

          # Initial Parameter guesses
          'sParams':{'A_ame':1,   # AME amplitude (unit)
                     'nu_mod':30, # AME centre frequency (GHz)
                     'EM':200 ,   # Emission measure of free-free
                     'dT': 26.91e-6, # CMB fluctuation amplitude  (unit)
                     'Tdust': 17.06, # Dust temperature amplitude (K)
                     'tau': -3.09,   # Dust opacity
                     'beta':  2.14}, # Spectral index of modified dust BB

          # Fitting information
          'frange':[0.,10000.], # Frequency range (GHz)s
          'FitErrs':[],
          'components':['sync', # Fit for synchrtron
                        'ff',   # ... free-free
                        'dust', # ... thermal dust
                        'ame'], # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': 'PerseusFlux.npy'   ,
          'ame_file': 'MC.dat'
          }


lorionis ={'name':'LOrionis',

          # Source apertures
          'theta': [-11.6],
          'phi': [-164.3],
          'ra': [5.2],
          'rb': [5.2],
          'pang':[-51.],
          'frac':[1./1.733],

          # Background apertures
          'itheta': [-11.6],
          'iphi': [-164.3],
          #'ira':[7.0],
          #'irb':[7.0],
          #'ipang':[-51.],
          #'ifrac':[1./1.346],

          'ira':[7],
          'irb':[7],
          'ipang':[-51.],
          'ifrac':[1./1.2],

          'isweep':[360.],

          # Initial Parameter guesses
          'sParams':{'A_ame':10,   # AME amplitude (unit)
                     'nu_mod':30, # AME centre frequency (GHz)
                     'EM':400 ,   # Emission measure of free-free
                     'dT': 26.91e-6, # CMB fluctuation amplitude  (unit)
                     'Tdust': 17.06, # Dust temperature amplitude (K)
                     'tau': -3.09,   # Dust opacity
                     'beta':  2.14}, # Spectral index of modified dust BB

          # Fitting information
          'frange':[0.,10000.], # Frequency range (GHz)
          'FitErrs':[],
          'components':['ff',   # ... free-free
                        'dust', # ... thermal dust
                        'ame'], # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': 'OrionisFlux.npy'   ,
          'ame_file': 'MC.dat'
          }


lorionisint ={'name':'LOrionis_Interior',

          # Source apertures
          'theta': [-11.6],
          'phi': [-164.3],
          'ra': [3.0],
          'rb': [3.0],
          'pang':[-51.],
          'frac':[0],

          # Background apertures
          'itheta': [-11.6],
          'iphi': [-164.3],
          #'ira':[7.0],
          #'irb':[7.0],
          #'ipang':[-51.],
          #'ifrac':[1./1.346],

          'ira':[8.0],
          'irb':[8.0],
          'ipang':[-51.],
          'ifrac':[0.8],

          'isweep':[360.],

          # Initial Parameter guesses
          'sParams':{'A_ame':10,   # AME amplitude (unit)
                     'nu_mod':30, # AME centre frequency (GHz)
                     'EM':0.0001 ,   # Emission measure of free-free
                     'dT': 26.91e-6, # CMB fluctuation amplitude  (unit)
                     'Tdust': 17.06, # Dust temperature amplitude (K)
                     'tau': -3.09,   # Dust opacity
                     'beta':  2.14}, # Spectral index of modified dust BB

          # Fitting information
          'frange':[0.,10000.], # Frequency range (GHz)
          'FitErrs':[],
          'components':['ff',   # ... free-free
                        'dust', # ... thermal dust
                        ], # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': 'OrionisFlux.npy'   ,
          'ame_file': 'MC.dat'
          }



lorionisint2 ={'name':'LOrionis_Interior2',

          # Source apertures
          'theta': [-11.6],
          'phi': [-164.3],
          'ra': [3.0],
          'rb': [3.0],
          'pang':[-51.],
          'frac':[0],

          # Background apertures
          'itheta': [-11.6,-11.6],
          'iphi': [-164.3,-164.3],
          'ira':[7.,7.],
          'irb':[7.,7.],
          'ipang':[-60.,+150.],
          'ifrac':[1./1.2,1./1.2],
          'isweep':[25.,40.],

          # Initial Parameter guesses
          'sParams':{'A_ame':10,   # AME amplitude (unit)
                     'nu_mod':30, # AME centre frequency (GHz)
                     'EM':0.0001 ,   # Emission measure of free-free
                     'dT': 26.91e-6, # CMB fluctuation amplitude  (unit)
                     'Tdust': 17.06, # Dust temperature amplitude (K)
                     'tau': -3.09,   # Dust opacity
                     'beta':  2.14}, # Spectral index of modified dust BB

          # Fitting information
          'frange':[0.,10000.], # Frequency range (GHz)
          'FitErrs':[],
          'components':['ff',   # ... free-free
                        'dust', # ... thermal dust
                        'ame'], # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': 'OrionisFlux.npy'   ,
          'ame_file': 'MC.dat'
          }





lorionis2 ={'name':'LOrionis2',

          # Source apertures
          'theta': [-11.6],
          'phi': [-164.3],
          'ra': [5.2],
          'rb': [5.2],
          'pang':[-51.],
           'frac':[1./1.733],

          # Background apertures
          'itheta': [-17.92,-7.265],
          'iphi': [-163.19,-169.03],
          'ira':[1.0,1.0],
          'irb':[1.0,1.0],
          'ipang':[-51.,-51.],
          'ifrac':[0.,0.],
          'isweep':[360.,360.],

          # Initial Parameter guesses
          'sParams':{'A_ame':1,   # AME amplitude (unit)
                     'nu_mod':30, # AME centre frequency (GHz)
                     'EM':200 ,   # Emission measure of free-free
                     'dT': 26.91e-6, # CMB fluctuation amplitude  (unit)
                     'Tdust': 17.06, # Dust temperature amplitude (K)
                     'tau': -3.09,   # Dust opacity
                     'beta':  2.14}, # Spectral index of modified dust BB

          # Fitting information
          'frange':[0.,10000.], # Frequency range (GHz)
          'FitErrs':[],
          'components':['ff',   # ... free-free
                        'dust', # ... thermal dust
                        'ame'], # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': 'OrionisFlux2.npy'   ,
          'ame_file': 'MC.dat'
          }



lorionis3 ={'name':'LOrionis3',

          # Source apertures
          'theta': [-11.6],
          'phi': [-164.3],
          'ra': [5.2],
          'rb': [5.2],
          'pang':[-51.],
           'frac':[1./1.733],

          # Background apertures
          'itheta': [-11.6,-11.6],
          'iphi': [-164.3,-164.3],
          'ira':[7.,7.],
          'irb':[7.,7.],
          'ipang':[-60.,+150.],
          'ifrac':[1./1.2,1./1.2],
          'isweep':[25.,40.],

          # Initial Parameter guesses
          'sParams':{'A_ame':1,   # AME amplitude (unit)
                     'nu_mod':30, # AME centre frequency (GHz)
                     'EM':200 ,   # Emission measure of free-free
                     'dT': 26.91e-6, # CMB fluctuation amplitude  (unit)
                     'Tdust': 17.06, # Dust temperature amplitude (K)
                     'tau': -3.09,   # Dust opacity
                     'beta':  2.14}, # Spectral index of modified dust BB

          # Fitting information
          'frange':[0.,10000.], # Frequency range (GHz)
          'FitErrs':[],
          'components':['ff',   # ... free-free
                        'dust', # ... thermal dust
                        'ame'], # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': 'OrionisFlux3.npy',
          'ame_file': 'WNM.dat'
          }





rosette = {'name':'Rosette',

          # Source apertures
          'theta': [-02.1172],
          'phi': [-153.5],
          'ra': [1.5],
          'rb': [1.5],
          'pang':[-51.],
          'frac':[0],

          # Background apertures
          'itheta': [-02.1172],
          'iphi': [-153.5],
          #'ira':[7.0],
          #'irb':[7.0],
          #'ipang':[-51.],
          #'ifrac':[1./1.346],

          'ira':[3.0],
          'irb':[3.0],
          'ipang':[-180.],
          'ifrac':[0.66666],

          'isweep':[60.],

          # Initial Parameter guesses
          'sParams':{'A_ame':10,   # AME amplitude (unit)
                     'nu_mod':30, # AME centre frequency (GHz)
                     'EM':0.0001 ,   # Emission measure of free-free
                     'dT': 26.91e-6, # CMB fluctuation amplitude  (unit)
                     'Tdust': 17.06, # Dust temperature amplitude (K)
                     'tau': -3.09,   # Dust opacity
                     'beta':  2.14}, # Spectral index of modified dust BB

          # Fitting information
          'frange':[0.,10000.], # Frequency range (GHz)
          'FitErrs':[],
          'components':['ff',   # ... free-free
                        'dust', # ... thermal dust
                        'ame'], # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': 'RosetteFlux.npy'   ,
          'ame_file': 'MC.dat'
          }




h1 ={'name':'B30',

          # Source apertures
          'theta': [-11.5],
          'phi': [-168.1],
          'ra': [2./1.5],
          'rb': [2./1.5],
          'pang':[-51.],
           'frac':[0],

          # Background apertures
          'itheta': [-11.6,-11.6],
          'iphi': [-164.3,-164.3],
          'ira':[7.,7.],
          'irb':[7.,7.],
          'ipang':[-60.,+150.],
          'ifrac':[1./1.2,1./1.2],
          'isweep':[25.,40.],

          # Initial Parameter guesses
          'sParams':{'A_ame':1,   # AME amplitude (unit)
                     'nu_mod':30, # AME centre frequency (GHz)
                     'EM':200 ,   # Emission measure of free-free
                     'dT': 26.91e-6, # CMB fluctuation amplitude  (unit)
                     'Tdust': 17.06, # Dust temperature amplitude (K)
                     'tau': -3.09,   # Dust opacity
                     'beta':  2.14}, # Spectral index of modified dust BB

          # Fitting information
          'frange':[0.,10000.], # Frequency range (GHz)
          'FitErrs':[],
          'components':['ff',   # ... free-free
                        'dust', # ... thermal dust
                        'ame'], # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': 'B30.npy'   ,
          'ame_file': 'WNM.dat'
          }

h2 ={'name':'B223',

          # Source apertures
          'theta': [-15.7],
          'phi': [-165.3],
          'ra': [2./1.5],
          'rb': [2./1.5],
          'pang':[-51.],
           'frac':[0],

          # Background apertures
          'itheta': [-11.6,-11.6],
          'iphi': [-164.3,-164.3],
          'ira':[7.,7.],
          'irb':[7.,7.],
          'ipang':[-60.,+150.],
          'ifrac':[1./1.2,1./1.2],
          'isweep':[25.,40.],

          # Initial Parameter guesses
          'sParams':{'A_ame':1,   # AME amplitude (unit)
                     'nu_mod':30, # AME centre frequency (GHz)
                     'EM':200 ,   # Emission measure of free-free
                     'dT': 26.91e-6, # CMB fluctuation amplitude  (unit)
                     'Tdust': 17.06, # Dust temperature amplitude (K)
                     'tau': -3.09,   # Dust opacity
                     'beta':  2.14}, # Spectral index of modified dust BB

          # Fitting information
          'frange':[0.,10000.], # Frequency range (GHz)
          'FitErrs':[],
          'components':['ff',   # ... free-free
                        'dust', # ... thermal dust
                        'ame'], # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': 'B223.npy'   ,
          'ame_file': 'WNM.dat'
          }


h3 ={'name':'Spur-Arm',

          # Source apertures
          'theta': [-11.8],
          'phi': [-160.4],
          'ra': [1.5/1.5],
          'rb': [1.5/1.5],
          'pang':[-51.],
           'frac':[0],

          # Background apertures
          'itheta': [-11.6,-11.6],
          'iphi': [-164.3,-164.3],
          'ira':[7.,7.],
          'irb':[7.,7.],
          'ipang':[-60.,+150.],
          'ifrac':[1./1.2,1./1.2],
          'isweep':[25.,40.],

          # Initial Parameter guesses
          'sParams':{'A_ame':1,   # AME amplitude (unit)
                     'nu_mod':30, # AME centre frequency (GHz)
                     'EM':200 ,   # Emission measure of free-free
                     'dT': 26.91e-6, # CMB fluctuation amplitude  (unit)
                     'Tdust': 17.06, # Dust temperature amplitude (K)
                     'tau': -3.09,   # Dust opacity
                     'beta':  2.14}, # Spectral index of modified dust BB

          # Fitting information
          'frange':[0.,10000.], # Frequency range (GHz)
          'FitErrs':[],
          'components':['ff',   # ... free-free
                        'dust', # ... thermal dust
                        'ame'], # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': 'Spur-Arm.npy'   ,
          'ame_file': 'WNM.dat'
          }

h4 ={'name':'LDN1598',

          # Source apertures
          'theta': [-9.2],
          'phi': [-161.3],
          'ra': [2.5/1.5],
          'rb': [2.5/1.5],
          'pang':[-51.],
           'frac':[0],

          # Background apertures
          'itheta': [-11.6,-11.6],
          'iphi': [-164.3,-164.3],
          'ira':[7.,7.],
          'irb':[7.,7.],
          'ipang':[-60.,+150.],
          'ifrac':[1./1.2,1./1.2],
          'isweep':[25.,40.],

          # Initial Parameter guesses
          'sParams':{'A_ame':1,   # AME amplitude (unit)
                     'nu_mod':30, # AME centre frequency (GHz)
                     'EM':200 ,   # Emission measure of free-free
                     'dT': 26.91e-6, # CMB fluctuation amplitude  (unit)
                     'Tdust': 17.06, # Dust temperature amplitude (K)
                     'tau': -3.09,   # Dust opacity
                     'beta':  2.14}, # Spectral index of modified dust BB

          # Fitting information
          'frange':[0.,10000.], # Frequency range (GHz)
          'FitErrs':[],
          'components':['ff',   # ... free-free
                        'dust', # ... thermal dust
                        'ame'], # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': 'LDN1598.npy'   ,
          'ame_file': 'WNM.dat'
          }

h5 ={'name':'Ring-Area',

          # Source apertures
          'theta': [-7.7],
          'phi': [-165.9],
          'ra': [2.5/1.5],
          'rb': [2.5/1.5],
          'pang':[-51.],
           'frac':[0],

          # Background apertures
          'itheta': [-11.6,-11.6],
          'iphi': [-164.3,-164.3],
          'ira':[7.,7.],
          'irb':[7.,7.],
          'ipang':[-60.,+150.],
          'ifrac':[1./1.2,1./1.2],
          'isweep':[25.,40.],

          # Initial Parameter guesses
          'sParams':{'A_ame':1,   # AME amplitude (unit)
                     'nu_mod':30, # AME centre frequency (GHz)
                     'EM':200 ,   # Emission measure of free-free
                     'dT': 26.91e-6, # CMB fluctuation amplitude  (unit)
                     'Tdust': 17.06, # Dust temperature amplitude (K)
                     'tau': -3.09,   # Dust opacity
                     'beta':  2.14}, # Spectral index of modified dust BB

          # Fitting information
          'frange':[0.,10000.], # Frequency range (GHz)
          'FitErrs':[],
          'components':['ff',   # ... free-free
                        'dust', # ... thermal dust
                        'ame'], # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': 'Ring-Area.npy'   ,
          'ame_file': 'WNM.dat'
          }


h6 ={'name':'Central-HII',

          # Source apertures
          'theta': [-12.00],
          'phi': [-164.95],
          'ra': [2./1.5],
          'rb': [2./1.5],
          'pang':[-51.],
           'frac':[0],

          # Background apertures
          'itheta': [-11.6,-11.6],
          'iphi': [-164.3,-164.3],
          'ira':[7.,7.],
          'irb':[7.,7.],
          'ipang':[-60.,+150.],
          'ifrac':[1./1.2,1./1.2],
          'isweep':[25.,40.],

          # Initial Parameter guesses
          'sParams':{'A_ame':1,   # AME amplitude (unit)
                     'nu_mod':30, # AME centre frequency (GHz)
                     'EM':200 ,   # Emission measure of free-free
                     'dT': 26.91e-6, # CMB fluctuation amplitude  (unit)
                     'Tdust': 17.06, # Dust temperature amplitude (K)
                     'tau': -3.09,   # Dust opacity
                     'beta':  2.14}, # Spectral index of modified dust BB

          # Fitting information
          'frange':[0.,10000.], # Frequency range (GHz)
          'FitErrs':[],
          'components':['ff',   # ... free-free
                        'dust'],#, # ... thermal dust
                        #'ame'], # ... spinning dust (add a second component?
          'AUX': None, # List of additional source fluxes from catalogue.
          'Output': 'Central-HII.npy',
          'ame_file': 'WNM.dat'
          }
