import numpy as np
from scipy.ndimage import binary_dilation, binary_erosion
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Generate data
x = np.linspace(10, 30, 1000)

# Subplots for carrier wave, pulse signal, and modulated wave
fig, ax = plt.subplots(5, 1, figsize=(15, 6))
plt.subplots_adjust(hspace=0.5)

# Carrier wave (sine wave)
carrier_frequency = 10
carrier_wave = np.sin(carrier_frequency * x)

# Plot for carrier wave
ax[0].plot(x, carrier_wave, label='Carrier Wave', color='red')
ax[0].set_title('Carrier Wave')
ax[0].set_ylim(-1.5, 1.5)
ax[0].tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
ax[0].legend()

# Parameters for pulse signals
pulse_amplitude = 1
pulse_width = 2.0



# Animation Function
def animate(frame):
    for axes in ax[1::]:
        axes.clear()
    
    # Pulse signal
    pulse_shift = frame * 0.1
    pulse_signal = (np.abs(x - pulse_shift) % pulse_width < pulse_width / 2).astype(float) * pulse_amplitude

    # OOK modulation
    modulated_wave = (carrier_wave * pulse_signal)

    # Noise
    np.random.seed(13213)
    noise_amplitude = 0.3 # Set the value to 0.0 to eliminate noise
    modulated_wave += np.random.normal(loc=0, scale=noise_amplitude, size=len(x)) * (pulse_signal > 0)

    # Threshold
    threshold = 0.1
    demodulated_wave = (modulated_wave > threshold).astype(float) *  pulse_amplitude
    demodulated_wave += (modulated_wave < -threshold).astype(float) *  pulse_amplitude

    # Threshold for binary signal
    binary_signal = (demodulated_wave > 0).astype(int)

    # Smoothening the binary signal using dialation and erosion
    smoothed_signal = binary_erosion(binary_dilation(binary_signal))

    # Plot the updated pulse signal
    ax[1].plot(x, pulse_signal, label='Pulse Signal', color='green')
    ax[1].set_title('Pulse Signal')
    ax[1].set_ylim(-0.5, 1.5)
    ax[1].legend()

    # Plot the updated modulated signal
    ax[2].plot(x, modulated_wave, color='blue')
    ax[2].set_title('OOK Modulated Wave')
    ax[2].set_ylim(-1.5, 1.5)
    # ax[2].legend()

    # Plot the updated demodulated signal
    ax[3].plot(x, demodulated_wave, label='Demodulated Wave', color='orange')
    ax[3].set_title('OOK Demodulated Wave')
    ax[3].set_ylim(-0.5, 1.5)
    ax[3].legend()

    # Plot the updated smoothed demodulated signal
    ax[4].plot(x, smoothed_signal, label='Smoothed Wave', color='green')
    ax[4].set_title('Smoothed Demodulated Wave')
    ax[4].set_ylim(-0.5, 1.5)
    ax[4].legend()

    for axes in ax:
        axes.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)


ani = FuncAnimation(fig, animate, frames=100, interval=50)

plt.show()
