# Aperture Photometry for HEALPix Maps

This repository offers tools for performing aperture photometry on HEALPix maps, enabling flux density measurements across diverse astrophysical applications. The code is modular and customizable.

---

## **Project Overview**

### Features:
- **Custom Aperture Shapes**: Supports elliptical and circular apertures with adjustable parameters.
- **Background Subtraction**: Configurable apertures for precise background estimation.
- **Map Units Handling**: Converts map units (e.g., `mK`, `MJy/sr`) to consistent flux units in Jy.
- **Error Estimation**: Accounts for calibration uncertainties and random noise.

### Typical Use Case:
Run photometry on HEALPix maps to extract source flux densities, analyze spectral energy distributions (SEDs), and handle ancillary data for astrophysical analysis.

---

## **Project Structure**

- **`photometry.py`**: Main script to perform aperture photometry.
- **`aperphot.py`**: Core photometry functions and utilities.
- **`bandpasses.py`**: Handles bandpass corrections and spectral adjustments.
- **`files.py`**: Defines input maps and their properties.
- **`source.py`**: Configures sources, apertures, and related settings.
- **`example_config/`**: Example configuration files and workflows.

---

## **Dependencies**

This project relies on the following Python packages:
- `healpy`
- `numpy`
- `matplotlib`
- `mpl_toolkits.mplot3d`

---

## **Quick Start Guide**

1. **Prepare Configuration**:
   - Copy `phot_config.py` from `example_config/` to your working directory.
   - Customize it for your maps, sources, and desired output.

2. **Define Input Maps**:
   - Edit `files.py` to specify paths, resolutions, and calibration uncertainties for each map.

3. **Set Up Sources**:
   - Use `source.py` to configure target sources and aperture settings.

4. **Run Photometry**:
   - Execute the following in your Python environment:
     ```python
     import photometry
     nu, flux, flux_err, source = photometry.photometry(
         custom_source=0, warnings_on=1, verbose=1
     )
     ```

5. **Analyze Results**:
   - Results include frequency, flux, and error for each source. Example output:
     ```
     FREQ = 1.42E+00   FLUX = 4.50E+01   ERR = 1.81E+01
     ```

---

## **Configuration Example**

A typical photometry configuration file includes:
- `mode`: Method for combining fluxes (e.g., `'median'`).
- `effective_beam_area`: Effective area in deg² for scaling.
- `maps`: List of input maps (defined in `files.py`).
- `targets`: List of sources to analyze (defined in `source.py`).

---

## **Terminal Output Example**

Here’s a snippet of typical photometry output:
```
*********************** SOURCE INFORMATION ***********************

SOURCE = S235, GALACTIC_COORDS = G+173.62+2.79
PRIMARY = [RA = 2.0, RB = 2.0, PANG = 0.0, FRAC = 0.0, AR = 12.6]
BCKGRND = [RA = 4.0, RB = 4.0, PANG = 0.0, FRAC = 0.7, AR = 25.6
           BACK_GALACTIC_COORDS = G+173.62+2.79, SWEEP = 360.0]


************** PHOTOMETRY INFORMATION *************

NFREQ = 25, NGOOD = 24, NEG = 0, ZERO = 0, NAN = 1
FREQ = 4.08E-01   FLUX = 9.39E+01   ERR = 3.87E+01
       1.42E+00          4.50E+01         1.81E+01
       2.33E+00          NAN              NAN
       1.10E+01          4.04E+01         1.21E+00
       1.30E+01          4.24E+01         1.27E+00
       1.70E+01          4.33E+01         7.80E+00
       1.90E+01          3.22E+01         9.03E+00
       2.28E+01          5.51E+01         5.51E-01
       3.30E+01          4.92E+01         4.92E-01
       4.07E+01          4.49E+01         4.49E-01
```

---


## Measuring Uncertainties

### Primary Flux Calculation
The primary flux is calculated by summing the pixel brightnesses within the primary aperture, subtracting the scaled background contribution:
$$F_{\text{primary}} = \sum_{i \in \text{aperture pixels}} I_i - \bar{F}_{\text{background}} \cdot N_{\text{primary}}$$
where:
- $I_i$ is the flux of pixel $i$ in the primary aperture.
- $\bar{F}_{\text{background}}$ is the mean flux of the background pixels.
- $N_{\text{primary}}$ is the number of pixels in the primary aperture.

### Background Flux and Variance
The background flux is estimated using either the mean or median of the background pixels:
$$\bar{F}_{\text{background}} = \frac{1}{N_{\text{background}}} \sum_{i \in \text{background pixels}} I_i$$
where $N_{\text{background}}$ is the number of background pixels.

The random variance in the background is scaled to the size of the primary aperture:
$$\sigma_{\text{background}}^2 = \left[\frac{1}{N_{\text{background}}} \sum_{i \in \text{background pixels}} (I_i^2) - \left(\frac{1}{N_{\text{background}}} \sum_{i \in \text{background pixels}} I_i \right)^2\right] \cdot N_{\text{primary}}$$

### Total Error Calculation
The total variance in the primary flux combines random and calibration variances:
$$\sigma_{\text{total}}^2 = \sigma_{\text{random}}^2 + \sigma_{\text{calibration}}^2$$
where:

- **Calibration Variance**:
  $$\sigma_{\text{calibration}}^2 = (F_{\text{primary}} \cdot \text{calibration error})^2$$

- **Random Variance** (scaled by beam area if necessary):
  $$\sigma_{\text{random}}^2 = \sigma_{\text{background}}^2 \cdot \frac{N_{\text{primary}}}{N_{\text{independent}}}$$
  where:
  - $N_{\text{independent}}$ is the number of independent beams in the primary aperture, given by:
    $$N_{\text{independent}} = \frac{\text{primary area (deg}^2\text{)}}{\text{effective beam area (deg}^2\text{)}}$$

### Dominance of Errors
- **High Signal-to-Noise Regions**: Calibration errors dominate.
- **Low Signal-to-Noise Regions**: Random noise dominates.


---

## **Advanced Options**


- **Custom Bandpasses**:
   - Modify `bandpasses.py` to handle instrument-specific colour corrections:
     ```python
     from bandpasses import fastmficc
     corrected_value = fastmficc(nu=17, alpha=0.1)
     ```

---


## 📜 Acknowledgements

This project is a joint effort between:

**Roke Cepeda-Arroita**  
Email: [roke.cepeda-arroita@manchester.ac.uk](mailto:roke.cepeda-arroita@manchester.ac.uk)

**Stuart Harper**  
_Email: [stuart.harper@manchester.ac.uk](mailto:stuart.harper@manchester.ac.uk)_

Version 2.0 [Dec 2024]



## **Contributing**

Contributions are welcome! Feel free to open issues or submit pull requests to improve functionality or documentation.

---

## **License**

This project is distributed under the MIT License.
