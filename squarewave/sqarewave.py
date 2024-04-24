import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
import pandas as pd

# Square wave generator function
def generate_square_wave(t, frequency, amplitude, num_harmonics, duty_cycle):
    square_wave = np.zeros_like(t)
    for n in range(1, num_harmonics + 1):
        harmonic = (4 / (2 * n - 1) / np.pi) * np.sin(2 * np.pi * (2 * n - 1) * frequency * t)
        square_wave += harmonic
    square_wave *= amplitude
    
    # Apply duty cycle
    period = 1 / frequency
    duty_cycle_time = (duty_cycle / 100) * period
    square_wave = np.where(t % period < duty_cycle_time, amplitude, -amplitude)
    
    return square_wave

# Data saver function
def save_to_csv(t, square_wave, filename):
    data = pd.DataFrame({
        'Time': t,
        'Amplitude': square_wave
    })
    data.to_csv(filename, index=False)
    print(f"Waveform data saved to {filename}")

# Default parameters
default_freq = 5.0
default_amp = 1.0
default_duty_cycle = 50.0  # Default duty cycle in percentage
samples = int(input("Enter the number of samples: "))
num_harmonics = 10000 # Number of harmonics to sum

# Time array for plotting
t = np.linspace(0, 1, samples, endpoint=False)

# Initial square wave
square_wave = generate_square_wave(t, default_freq, default_amp, num_harmonics, default_duty_cycle)

# Create plot
fig, ax = plt.subplots(figsize=(15, 10))
plt.subplots_adjust(bottom=0.35)
plt.title('Square Wave Generator')
ax.set_xlabel('Time (Sec)')
ax.set_ylabel('Amplitude')
plt.grid(True)

# Plot initial square wave
line, = plt.plot(t, square_wave, 'r', label='Generated Square Wave')
plt.legend()

# Add text boxes for frequency, amplitude, and duty cycle inputs
freq_text_box = widgets.TextBox(plt.axes([0.125, 0.05, 0.1, 0.05]), 'Freq', initial=str(default_freq))
amp_text_box = widgets.TextBox(plt.axes([0.325, 0.05, 0.1, 0.05]), 'Amp', initial=str(default_amp))
duty_cycle_text_box = widgets.TextBox(plt.axes([0.525, 0.05, 0.1, 0.05]), 'Duty (%)', initial=str(default_duty_cycle))

# Add a submit button
submit_button_ax = plt.axes([0.725, 0.05, 0.1, 0.05])
submit_button = widgets.Button(submit_button_ax, 'Save to CSV')

def update(val):
    freq = float(freq_text_box.text)
    amp = float(amp_text_box.text)
    duty_cycle = float(duty_cycle_text_box.text)
    new_square_wave = generate_square_wave(t, freq, amp, num_harmonics, duty_cycle)
    line.set_ydata(new_square_wave)
    
    # Update y-axis limits dynamically based on waveform amplitude range
    max_abs_amplitude = np.max(np.abs(new_square_wave))
    ax.set_ylim(-1.1 * max_abs_amplitude, 1.1 * max_abs_amplitude)
    
    plt.draw()

def submit_callback(event):
    freq = float(freq_text_box.text)
    amp = float(amp_text_box.text)
    duty_cycle = float(duty_cycle_text_box.text)
    save_to_csv(t, generate_square_wave(t, freq, amp, num_harmonics, duty_cycle), f'squarewave_{freq}_{amp}_{duty_cycle}.csv')

submit_button.on_clicked(submit_callback)
freq_text_box.on_submit(update)
amp_text_box.on_submit(update)
duty_cycle_text_box.on_submit(update)



plt.show()
