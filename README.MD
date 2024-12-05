STRUCTURE ***
The main script is photometry.py, which uses tools in aperphot.py and bandpasses.py. Paths and properties of input maps can be configured in files.py. Sources and apertures can be configured in source.py.

DEPENCENCIES ***
healpy, numpy, warnings, matplotlib, mpl_toolkits.mplot3d, os


6-STEP PHOTOMETRY GUIDE ***

1. Copy the phot_config.py file from example_config to your separate working directory.
Then configure this dummy configuration file with your own preferences.

2. Define your own "files.py" with the directory of your maps and their main properties.

3. Add/modify your sources in "source.py". See the example at the top for an explanation of what all the variables do.

4. Modify your preferences in "config_mcmc.py".

5. The photometry code can be run in a separate folder for convenience. To do this, in your separate working folder, import the photometry module into your script by using:

"import sys
sys.path.insert(0, photometry_folder)
import photometry, files, source, aperphot, bandpasses"

where photometry_folder is your path to the photometry code.

6. Query the program by using (for example):

"nu, flux, flux_err, source = photometry.photometry(custom_source=0, warnings_on=0, verbose=1)"
