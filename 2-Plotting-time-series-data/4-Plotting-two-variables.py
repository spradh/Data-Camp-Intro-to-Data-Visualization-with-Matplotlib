import matplotlib.pyplot as plt

# Initalize a Figure and Axes
fig, ax = plt.subplots()

# Plot the CO2 variable in blue
ax.plot(climate_change.index, climate_change["co2"], color = 'b')
ax.set_ylabel('CO2 (ppm)', color='b')

# Create a twin Axes that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature in red
ax2.plot(climate_change.index, climate_change["relative_temp"], color = 'r')
ax2.set_ylabel('Relative temperature (Celsius)', color = 'r')

plt.show()
