# Make sure to replace "#insert link here" with the actual link
tpf = TessTargetPixelFile("#insert link here")

# Display a single snapshot of the target pixel file
tpf.plot(frame_number=42)

# Convert the target pixel file to a light curve
light_curve = tpf.to_lightcurve(aperture_mask=tpf.pipeline_mask)
light_curve.plot()

# Flatten the light curve to remove trends
flattened_lc = light_curve.flatten()
flattened_lc.plot()

# Calculate the periodogram to find the dominant orbital period
periods = np.linspace(1, 5, 10000)
periodogram = light_curve.to_periodogram(method='bls', period=periods, frequency_factor=500)
periodogram.plot()

# Extract key parameters from the periodogram
orbital_period = periodogram.period_at_max_power
transit_midpoint = periodogram.transit_time_at_max_power
transit_duration = periodogram.duration_at_max_power

# Phase-fold the light curve using the discovered orbital period
folded_lc_ax = light_curve.fold(period=orbital_period, epoch_time=transit_midpoint).scatter()
folded_lc_ax.set_xlim(-3, 3)
