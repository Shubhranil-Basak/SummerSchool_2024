import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def generate_square_wave(t, frequency, amplitude, num_harmonics):
    square_wave = np.zeros_like(t)
    for n in range(1, num_harmonics + 1):
        harmonic = (4 / (2 * n - 1) / np.pi) * np.sin(2 * np.pi * (2 * n - 1) * frequency * t)
        square_wave += harmonic
    square_wave *= amplitude
    return square_wave

try:
    freq = input("Frequency (Default: 5Hz): ")
    freq = float(freq) if freq else 5.0

    amp = input("Amplitude (Default: 1 unit): ")
    amp = float(amp) if amp else 1.0

    samples = input("Sample rate per second (Default: 1000): ")
    samples = int(samples) if samples else 1000

    num_harmonics = input("Number of harmonics (Default: 10000): ")
    num_harmonics = int(num_harmonics) if num_harmonics else 10000

    if freq <= 0 or amp <= 0 or samples <= 0 or num_harmonics <= 0:
        raise ValueError("Frequency, amplitude, sample rate, and number of harmonics must be positive.")

except ValueError as e:
    print(f"Invalid input: {e}")
    exit()

# Time array for plotting
t = np.linspace(0, 1, samples, endpoint=False)

# Generate the square wave directly using summed sine waves
square_wave = generate_square_wave(t, freq, amp, num_harmonics)

# Plotting
plt.plot(t, square_wave, 'r', label='Generated Square Wave')
plt.title("Square Wave (Sum of Sine Waves)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

# Save data to CSV
data = pd.DataFrame(
    {
        'Time': t,
        'Amplitude': square_wave,
    }
)
data.to_csv('squarewave.csv', index=False)

plt.show()
