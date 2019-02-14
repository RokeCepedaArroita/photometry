# Configuration File

'''
Settings for target, maps, plots, data
'''

import numpy as np
import source
import files


## Select Target(s): this will be overwritten if you call photometry with a custom source!

targets = [source.perseus]  # see source.py for options


## Plot Options

save_aper = False   # turn on to produce aperture plots
save_hist = False   # turn on to produce histograms of the background
saveAperdir = '/scratch/nas_falcon/scratch/rca/projects/photometry/results' # where to save aperture plots


## Data Options

save_fluxes = '/scratch/nas_falcon/scratch/rca/projects/photometry/results' # where to save results


## Photometry options

mode = 'median'
throw_NaN = True


## Select Maps

maps = [files.haslam,
        #files.dwingeloo,
        files.Reich,
        #files.Jonas,
        #files.CBASS,
        files.quijote11,
        files.quijote13,
        files.quijote17,
        files.quijote19,
        files.wmapK,
        files.wmapKa,
        files.wmapQ,
        files.wmapV,
        files.wmapW,
        files.lfi30,
        files.lfi44,
        files.lfi70,
        files.hfi100,
        files.hfi143,
        files.hfi217,
	    files.hfi353,
        files.hfi545,
        files.hfi857,
	    files.dirbe6,
	    files.dirbe7,
        files.dirbe8,
        files.dirbe9,
	    files.dirbe10]
