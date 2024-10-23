import tkinter as tk
from tkinter import filedialog, StringVar, OptionMenu
from helper import read_signal_from_file, plot_one_signal

def add_signals(signal_list):

    sorted_indices = sorted(set(index for signal in signal_list for index, value in signal))
    
    summed_signal = {index: 0 for index in sorted_indices}
    
    for signal in signal_list:
        for index, value in signal:
            summed_signal[index] += value
    
    result_signal = [(index, summed_signal[index]) for index in sorted_indices]
    return result_signal

def subtract_signals(signal_list):
    reversed_signals = []
    for signal in signal_list[1:]:
        negated_signal = [(index, -value) for index, value in signal]
        reversed_signals.append(negated_signal)
        signals_to_add = [signal_list[0]] + reversed_signals
        return add_signals(signals_to_add)

def multiply_signal(signal_list, constant):
    return [(index, value * constant) for index, value in signal_list[0]]

def shift_signal(signal_list, k):
    return [(index - k, value) for index, value in signal_list[0]]

def reverse_signal(signal_list):
    return [(-index, value) for index, value in signal_list[0]]

# GUI Functions
def signal_processing_gui():

    root = tk.Tk()
    root.title("Signal Processing GUI")

    operation_var = StringVar(root)
    operation_var.set("Add")  # Default operation

    operation_dropdown = OptionMenu(root, operation_var, "Add", "Subtract", "Multiply Signal", "Shift Signal", "Reverse Signal")
    operation_dropdown.pack()

    m_label = tk.Label(root, text="Constant")
    m_label.pack()
    m_entry = tk.Entry(root)
    m_entry.pack()

    k_label = tk.Label(root, text="Shift value")
    k_label.pack()
    k_entry = tk.Entry(root)
    k_entry.pack()

    signals_list = []
    
    def load_signal():
        file_path = filedialog.askopenfilename()
        signal = read_signal_from_file(file_path)
        signals_list.append(signal)
        plot_one_signal(signal, title="Signal 1")
    
    load_button = tk.Button(root, text="Load Signal", command=load_signal)
    load_button.pack()

    def perform_operation():

        operation = operation_var.get()
        if operation == "Add":
            result = add_signals(signals_list)
            plot_one_signal(result, title="Result: Addition")
        elif operation == "Subtract":
            result = subtract_signals(signals_list)
            plot_one_signal(result, title="Result: Subtraction")
        elif operation == "Multiply Signal":
            try:
                constant = float(m_entry.get())  # Get multiplier constant from input
                result = multiply_signal(signals_list, constant)
                plot_one_signal(result, title=f"Result: Multiply Signal 1 by {constant}")
            except ValueError:
                print("Invalid constant for multiplication.")
        elif operation == "Shift Signal":
            try:
                k = int(k_entry.get())  # Get shift value from input
                result = shift_signal(signals_list, k)
                plot_one_signal(result, title=f"Result: Shift Signal 1 by {k}")
            except ValueError:
                print("Invalid value for shifting.")
        elif operation == "Reverse Signal":
            result = reverse_signal(signals_list)
            plot_one_signal(result, title="Result: Reverse Signal")
    operate_button = tk.Button(root, text="Perform Operation", command=perform_operation)
    operate_button.pack()

    root.mainloop()
