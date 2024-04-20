import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import binary_dilation, binary_erosion

def generate_waves(carrier_frequency, x, pulse_amplitude=1, pulse_width=2.0):
    # Generate modulated and demodulated waves
    carrier_wave = np.sin(carrier_frequency * x)
    pulse_signal = (np.abs(x) % pulse_width < pulse_width/2).astype(float) * pulse_amplitude
    modulated_wave = carrier_wave * pulse_signal

    # Adding noise
    np.random.seed(13213)
    noise_amplitude = 0.3
    modulated_wave += np.random.normal(loc=0, scale=noise_amplitude, size=len(x)) * (pulse_signal > 0)

    # Demodulation
    threshold = 0.1
    demodulated_wave = (modulated_wave > threshold).astype(float) * pulse_amplitude
    demodulated_wave += (modulated_wave < -threshold).astype(float) * pulse_amplitude

    # Smoothing the demodulated signal
    binary_signal = (demodulated_wave > 0).astype(int)
    smoothed_signal = binary_erosion(binary_dilation(binary_signal))

    return carrier_wave, pulse_signal, modulated_wave, demodulated_wave, smoothed_signal

def plot_waveforms(carrier_wave, pulse_signal, modulated_wave, demodulated_wave, smoothed_signal, x):
    # Create figure and axis for the plot
    fig, ax = plt.subplots(5, 1, figsize=(15, 10))

    # Plot carrier wave
    ax[0].plot(x, carrier_wave, color='red')
    ax[0].set_title('Carrier Wave')
    ax[0].set_ylim(-1.5, 1.5)

    # Plot pulse signal
    ax[1].plot(x, pulse_signal, color='green')
    ax[1].set_title('Pulse Signal')
    ax[1].set_ylim(-0.5, 1.5)

    # Plot modulated wave
    ax[2].plot(x, modulated_wave, color='blue')
    ax[2].set_title('OOK Modulated Wave')
    ax[2].set_ylim(-1.5, 1.5)

    # Plot demodulated wave
    ax[3].plot(x, demodulated_wave, color='orange')
    ax[3].set_title('OOK Demodulated Wave')
    ax[3].set_ylim(-0.5, 1.5)

    # Plot smoothed demodulated wave
    ax[4].plot(x, smoothed_signal, color='green')
    ax[4].set_title('Smoothed Demodulated Wave')
    ax[4].set_ylim(-0.5, 1.5)

    for axes in ax:
        axes.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)

    # Adjust layout
    plt.subplots_adjust(hspace=0.5)
    plt.show()
