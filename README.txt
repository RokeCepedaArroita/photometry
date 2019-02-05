STRUCTURE ***
The main script is photometry.py, which uses tools in aperphot.py and bandpasses.py. Paths and properties of input maps can be configured in files.py. Sources and apertures can be configured in source.py.

DEPENCENCIES ***
healpy, numpy, warnings, matplotlib, mpl_toolkits.mplot3d, os


3-STEP PHOTOMETRY GUIDE ***

1. Copy the phot_config.py file from example_config to your separate working directory.
Then configure this dummy configuration file with your own preferences.

2. In your separate working folder, import the photometry module into your script by using:

"import sys
sys.path.insert(0, photometry_folder)
import photometry, files, source, aperphot, bandpasses"

where photometry_folder is your path to the photometry code.

3. Query the program by using (example):

"nu, flux, flux_err, source = photometry.photometry(custom_source=0, warnings_on=0, verbose=1)"
