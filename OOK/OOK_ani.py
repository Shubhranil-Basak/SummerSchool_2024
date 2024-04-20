import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import binary_dilation, binary_erosion
from matplotlib.animation import FuncAnimation

def animate_waveforms(x):
    # Generate data
    carrier_frequency = 20
    carrier_wave = np.sin(carrier_frequency * x)

    fig, ax = plt.subplots(5, 1, figsize=(15, 6))
    plt.subplots_adjust(hspace=0.5)

    def animate(frame):
        for axes in ax[1:]:
            axes.clear()

        pulse_shift = frame * 0.1
        pulse_signal = (np.abs(x - pulse_shift) % 2.0 < 1.0).astype(float)

        modulated_wave = carrier_wave * pulse_signal

        np.random.seed(13213)
        noise_amplitude = 0.3
        modulated_wave += np.random.normal(loc=0, scale=noise_amplitude, size=len(x)) * (pulse_signal > 0)

        threshold = 0.1
        demodulated_wave = (modulated_wave > threshold).astype(float)
        demodulated_wave += (modulated_wave < -threshold).astype(float)

        binary_signal = (demodulated_wave > 0).astype(int)
        smoothed_signal = binary_erosion(binary_dilation(binary_signal))

        ax[0].clear()
        ax[0].plot(x, carrier_wave, color='red')
        ax[0].set_title('Carrier Wave')
        ax[0].set_ylim(-1.5, 1.5)

        ax[1].clear()
        ax[1].plot(x, pulse_signal, color='green')
        ax[1].set_title('Pulse Signal')
        ax[1].set_ylim(-0.5, 1.5)

        ax[2].clear()
        ax[2].plot(x, modulated_wave, color='blue')
        ax[2].set_title('OOK Modulated Wave')
        ax[2].set_ylim(-1.5, 1.5)

        ax[3].clear()
        ax[3].plot(x, demodulated_wave, color='orange')
        ax[3].set_title('OOK Demodulated Wave')
        ax[3].set_ylim(-0.5, 1.5)

        ax[4].clear()
        ax[4].plot(x, smoothed_signal, color='green')
        ax[4].set_title('Smoothed Demodulated Wave')
        ax[4].set_ylim(-0.5, 1.5)

        for axes in ax:
            axes.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)

    ani = FuncAnimation(fig, animate, frames=100, interval=50)
    plt.show()
