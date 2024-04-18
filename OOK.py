import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.ndimage import binary_dilation, binary_erosion

# Generate data
x = np.linspace(-10, 10, 1000)

# Carrier wave (sine wave)
carrier_frequency = 10
carrier_wave = np.sin(carrier_frequency * x)

# Generate a pulse signal (square wave) for OOK modulation
pulse_amplitude = 1
pulse_width = 2.0
pulse_signal = (np.abs(x) % pulse_width < pulse_width/2).astype(float) * pulse_amplitude

# Perform OOK modulation (carrier wave * pulse signal)
modulated_wave = (carrier_wave * pulse_signal)

# Noise
np.random.seed(42)
noise_amplitude = 0.1
modulated_wave += np.random.normal(loc=0, scale=noise_amplitude, size=len(x)) * (pulse_signal > 0)

# Threshold
threshold = 0.1
demodulated_wave = (modulated_wave > threshold).astype(float) *  pulse_amplitude
demodulated_wave += (modulated_wave < -threshold).astype(float) *  pulse_amplitude


# Create subplots for carrier wave, pulse signal, and modulated wave
fig, ax = plt.subplots(4, 1, figsize=(15, 6))

# Plot carrier wave
ax[0].plot(x, carrier_wave, label='Carrier Wave', color='red')
ax[0].set_title('Carrier Wave')

# Plot pulse signal (message wave)
ax[1].plot(x, pulse_signal, label='Pulse Signal', color='green')
ax[1].set_title('Pulse Signal')

# Plot modulated wave (OOK modulation)
ax[2].plot(x, modulated_wave, label='Modulated Wave', color='blue')
ax[2].set_title('OOK Modulated Wave')

# Plot demodulated wave (OOK demodulation)
ax[3].plot(x, demodulated_wave, label='Demodulated Wave', color='orange')
ax[3].set_title('OOK Demodulated Wave')


# Set ylim for each subplot
ax[0].set_ylim(-1.2, 1.2)
ax[1].set_ylim(-0.2, 1.2)
ax[2].set_ylim(-1.2, 1.2)
ax[3].set_ylim(-0.2, 1.2)
 

# Remove x ticks and labels for all subplots
for axes in ax:
    # axes.grid()
    axes.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)

# Adjust layout to add spacing between subplots
plt.subplots_adjust(hspace=0.5)

# Show legend for each subplot
for axes in ax:
    axes.legend()

# Show the plot
plt.show()
