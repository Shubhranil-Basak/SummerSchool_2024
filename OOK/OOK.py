import numpy as np
import OOK_ani
import OOK_static


def main():
    choice = input("Enter 1 for static plot or 2 for animation: ")
    x = np.linspace(10, 30, 1000)
    if choice == '1':
        # Static
        carrier_wave, pulse_signal, modulated_wave, demodulated_wave, smoothed_signal = OOK_static.generate_waves(
            carrier_frequency=20, x=x, pulse_amplitude=1, pulse_width=2.0)
        OOK_static.plot_waveforms(carrier_wave, pulse_signal, modulated_wave, demodulated_wave, smoothed_signal, x)
    elif choice == '2':
        # Animation
        OOK_ani.animate_waveforms(x)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
