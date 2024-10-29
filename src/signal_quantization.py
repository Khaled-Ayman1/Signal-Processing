# import numpy as np
# from tkinter import Tk, Label, Entry, Button, messagebox, filedialog
# import matplotlib.pyplot as plt
# from helper import plot_one_signal, plot_quantized_signal, read_signal_from_file

# def quantize_signal(signal, num_levels=None, num_bits=None):
#     if num_bits is not None:
#         num_levels = 2 ** num_bits
#     elif num_levels is None:
#         raise ValueError("Either num_levels or num_bits must be provided.")

#     signal_val = [tup[1] for tup in signal]

#     min_val, max_val = np.min(signal_val), np.max(signal_val)
#     step_size = (max_val - min_val) / (num_levels - 1)
    
#     quantization_levels = np.array([min_val + i * step_size for i in range(num_levels + 1)])

#     quantized_signal = np.array([quantization_levels[np.argmin(np.abs(quantization_levels - val))] for val in signal_val])

#     # Calculate quantization error
#     quantization_error = signal_val - quantized_signal

#     binary_length = int(np.ceil(np.log2(num_levels)))
#     encoded_signal = {level: format(i, f'0{binary_length}b') for i, level in enumerate(quantization_levels)}

#     # Pair the encoded values with quantized signal
#     encoded_quantized_signal = [(encoded_signal[val], val) for val in quantized_signal]

#     return encoded_quantized_signal, quantization_error


# def quantization(signal, root, levels_entry=None, bits_entry=None):
#     # Get user input
#     num_levels = int(levels_entry.get()) if levels_entry.get() else None
#     num_bits = int(bits_entry.get()) if bits_entry.get() else None

#     # Ensure at least one input is provided
#     if num_levels is None and num_bits is None:
#         messagebox.showwarning("Input Error", "Please enter either levels or bits.")
#         return

#     # Quantize the signal
#     quantized_signal, quantization_error = quantize_signal(signal, num_levels, num_bits)

#     plot_quantized_signal(signal, quantized_signal, quantization_error, root)

# def signal_quantization_gui():
#     root = Tk()
#     root.title("Signal Quantization")

#     # Input Fields for Levels and Bits
#     Label(root, text="Number of Levels:").grid(row=0, column=0, padx=5, pady=5)
#     levels_entry = Entry(root)
#     levels_entry.grid(row=0, column=1, padx=5, pady=5)

#     Label(root, text="Number of Bits:").grid(row=1, column=0, padx=5, pady=5)
#     bits_entry = Entry(root)
#     bits_entry.grid(row=1, column=1, padx=5, pady=5)

#     # Load Signal Button
#     signal_list = []
#     def load_signal():
#         file_path = filedialog.askopenfilename()
#         signal = read_signal_from_file(file_path)
#         plot_one_signal(signal, title="Signal")
#         signal_list.append(signal)

#     load_button = Button(root, text="Load Signal", command=load_signal)
#     load_button.grid(row=2,column=0, columnspan=2, pady=10)
#     # Quantize Button
#     generate_button = Button(root, text="Quantize Signal", command=lambda: quantization(signal_list[0], root, levels_entry, bits_entry))
#     generate_button.grid(row=3, column=0, columnspan=2, pady=10)

#     root.mainloop()

import numpy as np
from tkinter import Tk, Label, Entry, Button, messagebox, filedialog
import matplotlib.pyplot as plt
from helper import plot_one_signal, plot_quantized_signal, read_signal_from_file

def quantize_signal(signal, num_levels=None, num_bits=None):
    # Determine num_levels if num_bits is provided
    if num_bits is not None:
        num_levels = 2 ** num_bits
    elif num_levels is None:
        raise ValueError("Either num_levels or num_bits must be provided.")

    # Extract signal values and calculate min/max
    signal_values = np.array([tup[1] for tup in signal])
    min_val, max_val = np.min(signal_values), np.max(signal_values)
    
    # Calculate step size
    step_size = (max_val - min_val) / num_levels
    
    # Generate quantization levels
    quantization_levels = [min_val + i * step_size for i in range(num_levels)]
    
    # Quantize each value to the nearest quantization level
    quantized_signal = np.array([quantization_levels[np.argmin(np.abs(np.array(quantization_levels) - val))] for val in signal_values])
    
    # Calculate quantization error
    quantization_error = signal_values - quantized_signal

    # Create binary encoding for each unique quantized level
    unique_quantized_levels = sorted(set(quantized_signal))
    binary_length = int(np.ceil(np.log2(len(unique_quantized_levels))))
    encoded_signal = {level: format(i, f'0{binary_length}b') for i, level in enumerate(unique_quantized_levels)}

    # Pair the encoded values with quantized signal
    encoded_quantized_output = [(encoded_signal[val], val) for val in quantized_signal]
    return encoded_quantized_output, quantization_error

def quantization(signal, levels_entry, bits_entry, root):
    # Get user input
    num_levels = int(levels_entry.get()) if levels_entry.get() else None
    num_bits = int(bits_entry.get()) if bits_entry.get() else None

    # Ensure at least one input is provided
    if num_levels is None and num_bits is None:
        messagebox.showwarning("Input Error", "Please enter either levels or bits.")
        return

    # Quantize the signal
    encoded_quantized_output, quantization_error = quantize_signal(signal, num_levels, num_bits)

    # Display results
    output = "\n".join([f"{code} {value:.2f}" for code, value in encoded_quantized_output])
    print("Encoded Quantized Output:")
    print(output)

    plot_quantized_signal(signal, [val for _, val in encoded_quantized_output], quantization_error, encoded_quantized_output, root)

def signal_quantization_gui():
    root = Tk()
    root.title("Signal Quantization")

    # Input Fields for Levels and Bits
    Label(root, text="Number of Levels:").grid(row=0, column=0, padx=5, pady=5)
    levels_entry = Entry(root)
    levels_entry.grid(row=0, column=1, padx=5, pady=5)

    Label(root, text="Number of Bits:").grid(row=1, column=0, padx=5, pady=5)
    bits_entry = Entry(root)
    bits_entry.grid(row=1, column=1, padx=5, pady=5)

    # Load Signal Button
    signal_list = []
    def load_signal():
        file_path = filedialog.askopenfilename()
        signal = read_signal_from_file(file_path)
        plot_one_signal(signal, title="Signal")
        signal_list.append(signal)

    load_button = Button(root, text="Load Signal", command=load_signal)
    load_button.grid(row=2, column=0, columnspan=2, pady=10)

    # Quantize Button
    generate_button = Button(root, text="Quantize Signal", command=lambda: quantization(signal_list[0], levels_entry, bits_entry, root))
    generate_button.grid(row=3, column=0, columnspan=2, pady=10)

    root.mainloop()
