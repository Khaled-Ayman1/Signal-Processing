import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt

def read_signal_from_file(file_path):
    signal = []
    with open(file_path, 'r') as file:
        N = int(file.readline().strip())  # Read number of samples
        for _ in range(N):
            index, value = map(float, file.readline().strip().split())
            signal.append((index, value))
    return signal

def load_signal():
    file_path = filedialog.askopenfilename()
    signal = read_signal_from_file(file_path)
    for (index, value) in signal:
        print(index, value)  
    plot_signal(signal, title="Loaded Signal")

def add_signals(*signals):
    result = [(idx, sum(val for _, val in sample)) for sample in zip(*signals)]
    return result

def multiply_signal(signal, constant):
    return [(index, value * constant) for index, value in signal]

def subtract_signals(signal1, signal2):
    return add_signals(signal1, multiply_signal(signal2, -1))

def shift_signal(signal, k):
    return [(index + k, value) for index, value in signal]

def reverse_signal(signal):
    return [(-index, value) for index, value in signal]

def plot_signal(signal, title="Signal"):
    indices = [point[0] for point in signal]
    values = [point[1] for point in signal]
    plt.figure()
    plt.plot(indices, values, marker='o')
    plt.title(title)
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.grid(True)
    plt.show()

def create_gui():
    root = tk.Tk()
    root.title("Signal Processing GUI")

    load_button = tk.Button(root, text="Load Signal", command=load_signal)
    load_button.pack()

    root.mainloop()

create_gui()