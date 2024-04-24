import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Constants and initial conditions
R0 = 100  # Initial resistance at room temperature (ohms)
alpha = 0.00392  # Temperature coefficient of resistance for a typical metal (ohms/°C)
V0 = 10  # Initial voltage across the resistor (volts)
I0 = V0/R0  # Initial current through the resistor (amps)

# Simulation parameters
num_steps = 100  # Number of temperature steps
delta_T = 5  # Temperature increment per step (°C)

# Initialize arrays to store temperature, resistance, and current values
temperatures = np.zeros(num_steps)
resistances = np.zeros(num_steps)
currents = np.zeros(num_steps)

# Perform initial simulation to populate arrays
current_temperature = 25
for i in range(num_steps):
    power = I0**2 * R0
    delta_temperature = power / (alpha * R0)
    current_temperature += delta_temperature
    current_resistance = R0 * (1 + alpha * (current_temperature - 25))
    current_current = np.sqrt(power / current_resistance)
    temperatures[i] = current_temperature
    resistances[i] = current_resistance
    currents[i] = current_current
    current_temperature += delta_T

# Create figure and axis for the plot
fig, ax = plt.subplots(figsize=(8, 6))
plt.subplots_adjust(left=0.125, right=0.9, bottom=0.15, top=0.92, wspace=0.2, hspace=0.2)


# Plot resistance vs. temperature
color = 'tab:red'
line_resistance, = ax.plot(temperatures, resistances, marker='o', linestyle='-', color=color)
ax.set_xlabel('Temperature (°C)')
ax.set_ylabel('Resistance (ohms)', color=color)
ax.tick_params(axis='y', labelcolor=color)

# Create a second y-axis for current
ax2 = ax.twinx()
color = 'tab:blue'
line_current, = ax2.plot(resistances, currents, marker='x', linestyle='--', color=color)
ax2.set_ylabel('Current (amps)', color=color)
ax2.tick_params(axis='y', labelcolor=color)

# Add titles and grid
plt.title('Resistance vs. Temperature with Current vs. Resistance')
plt.grid(True)

# Define slider positions within the same figure with adjusted spacing
ax_I0 = plt.axes([0.2, 0.050, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_R0 = plt.axes([0.2, 0.005, 0.65, 0.03], facecolor='lightgoldenrodyellow')

# Create sliders within the same figure with adjusted spacing
slider_V0 = Slider(ax_I0, 'Initial Voltage (V)', 1.0, 100, valinit=V0)
slider_alpha = Slider(ax_R0, 'alpha (ohms/°C)', 0.0001, 0.01, valinit=alpha)

# Define update function for sliders
def update(val):
    R0  # Use the global keyword to modify the global R0 variable
    # Update simulation parameters
    V0 = slider_V0.val
    I0 = V0/R0
    alpha = slider_alpha.val

    # Re-simulate based on new parameters
    current_temperature = 25
    for i in range(num_steps):
        power = I0**2 * R0
        delta_temperature = power / (alpha * R0)
        current_temperature += delta_temperature
        current_resistance = R0 * (1 + alpha * (current_temperature - 25))
        current_current = np.sqrt(power / current_resistance)
        temperatures[i] = current_temperature
        resistances[i] = current_resistance
        currents[i] = current_current
        current_temperature += delta_T

    # Update plot data
    line_resistance.set_xdata(temperatures)  # Update x-data for resistance plot
    line_resistance.set_ydata(resistances)   # Update y-data for resistance plot
    line_current.set_xdata(temperatures)     # Update x-data for current plot
    line_current.set_ydata(currents)         # Update y-data for current plot

    # Update plot limits if necessary
    ax.relim()
    ax.autoscale_view()
    ax2.relim()
    ax2.autoscale_view()

    # Redraw the plot
    fig.canvas.draw_idle()

# Connect sliders to update function
slider_V0.on_changed(update)
slider_alpha.on_changed(update)

plt.show()