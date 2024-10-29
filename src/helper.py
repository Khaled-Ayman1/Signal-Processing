import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def read_signal_from_file(file_path):
    signal = []
    with open(file_path, 'r') as file:
        file.readline()
        file.readline()
        N = int(file.readline().strip())  # Read number of samples
        for _ in range(N):
            index, value = map(float, file.readline().strip().split())
            signal.append((index, value))
    return signal

def plot_one_signal(signal, title="Signal"):
    indices = [point[0] for point in signal]
    values = [point[1] for point in signal]
    
    plt.figure()
    plt.plot(indices, values, marker='o')
    plt.title(title)
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.grid(True)
    plt.show()

def plot_two_signals(signal1, label1, representation_1, multi, signal2, label2, representation_2):
    t1, y1 = signal1

    plt.figure()
    
    if representation_1 == 1:
        plt.plot(t1, y1, label=label1)
    else:
        plt.stem(t1, y1, label=label1, basefmt=" ", linefmt='r-', markerfmt='ro')

    if multi == True:
        t2, y2 = signal2
        if representation_2 == 1:
            plt.plot(t2, y2, label=label2)
        else:
            plt.stem(t2, y2, label=label2, basefmt=" ", linefmt='g-', markerfmt='go')

    plt.title("Signal Generation")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid()
    plt.show()

def plot_quantized_signal(signal, quantized_signal, quantization_error, root):

    t1 = [tup[0] for tup in signal]
    y1 = [tup[1] for tup in signal]

    t2 = [tup[0] for tup in quantized_signal]
    y2 = [tup[1] for tup in quantized_signal]

    plt.figure()
    plt.plot(t1, y1, label= "Signal", marker='o')
    plt.stem(t1, y2, label="Quantized Signal", basefmt=" ", linefmt='g-', markerfmt='go')

    plt.title("Signal Quantization")
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid()
    plt.show()
    
    # fig, axs = plt.subplots(2, 1, figsize=(5, 5))
    # canvas = FigureCanvasTkAgg(fig, root)
    # canvas.get_tk_widget().grid(row=4, column=0, columnspan=2)

    # # Plot original and quantized signals
    # axs[0].clear()
    # axs[0].plot(signal, label="Original Signal", color="blue", alpha=0.7)
    # axs[0].plot(quantized_signal, label="Quantized Signal", color="red", linestyle='--')
    # axs[0].set_title("Original vs Quantized Signal")
    # axs[0].legend()

    # # Plot quantization error
    # axs[1].clear()
    # axs[1].plot(quantization_error, label="Quantization Error", color="purple")
    # axs[1].set_title("Quantization Error")
    # axs[1].legend()

    # canvas.draw()

    # Display encoded signal in the console
    print("Encoded Signal:", t2)
    print("Quantized Signal:", y2)