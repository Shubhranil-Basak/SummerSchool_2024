import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import pandas as pd

# Prompt user for frequency, amplitude, and sample rate per second
try:
    freq = float(input("Frequency (Hz): "))
    amp = float(input("Amplitude: "))
    samples = int(input("Sample rate per second: "))
    
    if freq <= 0 or amp <= 0 or samples <= 0:
        raise ValueError("Frequency, amplitude, and sample rate must be positive numbers.")
except ValueError as e:
    print(f"Invalid input: {e}")
    exit()

# Generate time array
t = np.linspace(0, 1, samples, endpoint=False)

amplitude = signal.square(2 * np.pi * freq * t) * amp

#DataFrame using Pandas
data = pd.DataFrame({
    'Time': t,
    'Amplitude': amplitude,
})


# Generate and plot the square wave
plt.plot(t, amplitude)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title(f"Square Wave: Frequency = {freq} Hz, Amplitude = {amp}")
plt.ylim(-2 * amp, 2 * amp)
plt.grid(True)
plt.show()

#Saving the CSV file
data.to_csv('square_wave.csv', index=False)

