# Make sure to install the required packages
# pip install lightkurve

from lightkurve import search_targetpixelfile
from lightkurve import TessTargetPixelFile
import lightkurve as lk
import numpy as np

# Search for the target pixel file
target_id = 'KIC 6922244'
cadence_type = "long"
quarter = 4
pixel_file = search_targetpixelfile(target_id, author="Kepler", cadence=cadence_type, quarter=quarter).download()

# Plot the pixel file
pixel_file.plot(frame=42)

# Convert the pixel file to light curve
lc = pixel_file.to_lightcurve(aperture_mask=pixel_file.pipeline_mask)
lc.plot()

# Flatten the light curve
flat_lc = lc.flatten()
flat_lc.plot()

# Fold the flattened light curve
period_of_interest = 3.5225
folded_lc = flat_lc.fold(period=period_of_interest)
folded_lc.plot()

# Calculate periodogram using Box Least Squares
periods = np.linspace(1, 5, 10000)
bls_periodogram = lc.to_periodogram(method='bls', period=periods, frequency_factor=500)
bls_periodogram.plot()

# Find key parameters from the periodogram
planet_x_period = bls_periodogram.period_at_max_power
planet_x_t0 = bls_periodogram.transit_time_at_max_power
planet_x_duration = bls_periodogram.duration_at_max_power

# Plot folded light curve
folded_ax = lc.fold(period=planet_x_period, epoch_time=planet_x_t0).scatter()
folded_ax.set_xlim(-2, 2)

# Print results
print("Detected Planet Period:", planet_x_period)
print("Transit Midpoint Time:", planet_x_t0)
print("Transit Duration:", planet_x_duration)
