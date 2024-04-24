import matplotlib.pyplot as plt

VOLTAGE = 8.84
current = [0.09, 8.71, 0.88, 0.09, 8.77, 8.78, 0.18, 1.40]
resistance = [96.30, 0.96, 9.79, 97.60, 0.95, 0.92, 45.80, 4.90]
resistance_inv = [0.01, 1.04, 0.10, 0.01, 1.05, 1.09, 0.02, 0.20]

# Combine the lists into tuples
combined_data = list(zip(current, resistance, resistance_inv))

# Sort the combined data based on resistance (second element in each tuple)
sorted_data = sorted(combined_data, key=lambda x: x[1])

# Unzip the sorted data back into separate lists
sorted_current, sorted_resistance, sorted_resistance_inv = zip(*sorted_data)

calculated_current = [VOLTAGE / r for r in sorted_resistance]

# Plot the sorted data
plt.plot(sorted_resistance_inv, sorted_current, 'b--', marker='o')
plt.plot(sorted_resistance_inv, calculated_current, 'r-')
plt.ylabel('Current (mA)')
plt.xlabel('Resistance inverse (1/KΩ)')
plt.title("Ohm's Law")
plt.show()
