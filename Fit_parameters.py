### Cepheids
include_Cepheids = False
N_galaxies_Cep = 19         # Number of SN-host galaxies
N_anchors_Cep = 2           # Number of anchors
include_MW = True           # Considers the MW-Cepheids and their GAIA parallax
fixed_zp = False            # False -> Fit for the GAIA zp
zp = 0.14                   # GAIA zp in μas, ONLY IF fixed_zp = True
fixed_Zw = False            # False -> Fit for the metallicity effect on the PLR
Zw = 0                      # Slope of the metallicity effect on the PLR ONLY IF fixed_Zw = True
PLR_break = False            # Allows for a break in the PLR at P=10d
break_P = 10                # Period of the PLR-break ONLY IF PLR_break = True
added_scatter = 0.0682      # Add dispersion to the Cepheids (0.0682 in Moertsell et al. 2021)
outlier_rejection = True    # 2.7-clipping process
RLB_correction = True       # Correct for the RLB (Anderson 2019)
Kcorr_Cep = False           # Correct for the K-corrections (Anderson 2021)


### TRGB
include_TRGB = True
N_galaxies_TRGB = 15        # Number of SN-host galaxies
N_anchors_TRGB = 1          # Number of anchors
Kcorr_TRGB = False          # Correct for the K-corrections (Anderson 2021)
use_color = True            # Consider or not the color (V-I) of the TRGB (like Anand 2021)
mid_VI = 1.32               # zero point for the color term (1.32 corresponds to the value for N4258 from Anand (2021)


### Cepheids + TRGB (only if include_Ceph & include_TRGB = True)
different_mu = False         # Allows a different distance for mu_Cep and mu_TRGB
different_MB = False         # Allows a different magnitude for MB_Cep and MB_TRGB

### SNe
fit_aB = True
a_B = 0.715840              # Value for the Hubble diagram's intercept ONLY IF fit_aB = False
sig_a_B = 0.001631          # 0.71273 +/- 0.00176 Riess 2016, OR can be fitted
z_min = 0.023               # Min redshift to consider when fitting for a_B
z_max = 0.15               # Max redshift to consider when fitting for a_B
### Wesenheit
R = 0.386

### Physics constants
c = 299792.458              # km/s
q0 = -0.55
j0 = 1
