import matplotlib.pyplot as plt

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