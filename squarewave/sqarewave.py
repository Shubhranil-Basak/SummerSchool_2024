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


# Time array for plotting
t = np.linspace(0, 1, samples, endpoint=False)

# Scale time array to match the specified frequency
x = 2 * np.pi * freq * t

if fourier.lower() in ['y', 'yes']:
    # Number of Fourier series terms
    try:
        n = (input("Maximum degree of the forier sum polynomial (Default: 70): "))
        if n == "":
            n = int(70)
        else:
            n = int(n)
        if n <= 0:
            raise ValueError("Degree of polynomial should be a positive integer")
    except ValueError as e:
        print(f"Invalid input: {e}")
        exit()
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

    fig, ax =  plt.subplots(1, 2, figsize=(15, 15))

    ax[0].plot(t, sum_series, 'g', label='Fourier Approximation')
    ax[0].set_title("Square wave (fourier series)")
    ax[1].plot(t, amp * square_wave(x), 'r', label='Original Square Wave')
    ax[1].set_title("Square wave")

    for axes in ax:
        axes.grid()
        axes.set_xlabel("Time (s)")
        axes.set_ylabel("Amplitude")
        axes.legend()

    data = pd.DataFrame({
    'Time': t,
    'Amplitude': sum_series,
    })
    data.to_csv('squarewave_fourier.csv', index=False)



else:
    amplitude = square(x) * amp
    plt.plot(t, amplitude, 'r', label='Original Square Wave')
    plt.title("Square Wave")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")

    data = pd.DataFrame({
    'Time': t,
    'Amplitude': amplitude,
    })
    data.to_csv('squarewave_fourier.csv', index=False)



# Plot the graph


plt.show()


data.to_csv('squarewave_fourier.csv', index=False)