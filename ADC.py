import tkinter as tk

def calculate():
    N = entry1.get()
    AIV = entry2.get()
    RV = entry3.get()
    try:
        N = float(N)
        AIV = float(AIV)
        RV = float(RV)

        if (RV > 0 and AIV >= 0) or (RV < 0 and AIV <= 0) :
            result1 = int(((2**N)*(AIV))/(RV))
            result2 = bin(result1)[2::]
        elif RV < 0 or AIV < 0:
            result1 = int(((2**N)*(AIV))/(RV))
            result2 = '-' + bin(result1)[3::]
        elif RV == 0 and AIV != 0:
            result1 = "infinity"
            result2 = "infinity"
        elif AIV == 0 and RV == 0:
            result1 = "NaN"
            result2 = "NaN"

        # Update the text in the output Entry widgets
        output_entry1.delete(0, tk.END)
        output_entry1.insert(0, result1)

        output_entry2.delete(0, tk.END)
        output_entry2.insert(0, result2)

    except ValueError:
        #Error message for invalid input
        output_entry1.delete(0, tk.END)
        output_entry1.insert(0, "Invalid input")

        output_entry2.delete(0, tk.END)
        output_entry2.insert(0, "Invalid input")

def reset():
    # Reset all input fields to empty strings
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)

    # Reset output Entry widgets to empty strings
    output_entry1.delete(0, tk.END)
    output_entry2.delete(0, tk.END)


# Main tkinter window
root = tk.Tk()
root.title("ADC Calculator")


# Main frame
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()


# Input fields
tk.Label(frame, text="Number of bits in ADC:").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(frame)
entry1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Analog Voltage input to ADC:").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(frame)
entry2.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text="Reference voltage to ADC:").grid(row=2, column=0, padx=10, pady=5)
entry3 = tk.Entry(frame)
entry3.grid(row=2, column=1, padx=10, pady=5)


# Output Entry widgets
tk.Label(frame, text="Numeric Digital Output:").grid(row=3, column=0, padx=10, pady=5)
output_entry1 = tk.Entry(frame)
output_entry1.grid(row=3, column=1, padx=10, pady=5)

tk.Label(frame, text="Binary Digital Output:").grid(row=4, column=0, padx=10, pady=5)
output_entry2 = tk.Entry(frame)
output_entry2.grid(row=4, column=1, padx=10, pady=5)


# Calculate and Reset buttons
calculate_button = tk.Button(frame, text="Calculate", command=calculate)
calculate_button.grid(row=5, column=0, padx=10, pady=10)

reset_button = tk.Button(frame, text="Reset", command=reset)
reset_button.grid(row=5, column=1, padx=10, pady=10)


# Tkinter mainloop
root.mainloop()
