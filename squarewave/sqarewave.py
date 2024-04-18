import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square
from scipy.integrate import quad
import pandas as pd


# Define the square wave function
def square_wave(x):
    return square(x)

try:
    freq = input("Frequency (Default: 5Hz): ")
    if freq == "":
        freq = float(5)
    else:
        freq = float(freq)

    amp = input("Amplitude (Default: 1 unit): ")
    if amp == "":
        amp = float(1)
    else:
        amp = float(amp)

    samples = input("Sample rate per second (Default: 1000): ")
    if samples == "":
        samples = int(1000)
    else:
        samples = int(samples)

    fourier = input("Do you want fourier series based square waves?(Y/N): ")
    
    if freq <= 0 or amp <= 0 or samples <= 0:
        raise ValueError("Frequency, amplitude, and sample rate must be positive numbers.")
except ValueError as e:
    print(f"Invalid input: {e}")
    exit()

# Number of Fourier series terms
n = 70

# Time array for plotting
t = np.linspace(0, 1, samples, endpoint=False)

# Scale time array to match the specified frequency
x = 2 * np.pi * freq * t

if fourier.lower() in ['y', 'yes']:
    # Compute Fourier coefficients
    An = []
    Bn = []

    for i in range(1, n+1):
        fc = lambda x: square_wave(x) * np.cos(i * x)
        fs = lambda x: square_wave(x) * np.sin(i * x)
        
        an, _ = quad(fc, 0, 2*np.pi)
        bn, _ = quad(fs, 0, 2*np.pi)
        
        An.append(an / np.pi)
        Bn.append(bn / np.pi)

    # Compute Fourier series summation
    sum_series = np.zeros_like(t)
    for i in range(1, n+1):
        sum_series += An[i-1] * np.cos(i * x) + Bn[i-1] * np.sin(i * x)

    # Scale the Fourier series summation by the specified amplitude
    sum_series *= amp
    plt.plot(t, sum_series, 'g', label='Fourier Series Approximation')
    plt.plot(t, amp * square_wave(x), 'r--', label='Original Square Wave')
    plt.title("Fourier Series for Square Wave")

    data = pd.DataFrame({
    'Time': t,
    'Amplitude': sum_series,
    })
    data.to_csv('squarewave_fourier.csv', index=False)



else:
    amplitude = square(x) * amp
    plt.plot(t, amplitude, 'r', label='Original Square Wave')
    plt.title("Square Wave")

    data = pd.DataFrame({
    'Time': t,
    'Amplitude': amplitude,
    })
    data.to_csv('squarewave_fourier.csv', index=False)



# Plot the graph
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.show()


data.to_csv('squarewave_fourier.csv', index=False)