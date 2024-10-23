import numpy as np
from tkinter import StringVar, OptionMenu, Label, Entry, Button, Toplevel, Radiobutton, IntVar
from helper import plot_two_signals

def generate_signal(signal_type, amplitude, phase_shift, frequency, sampling_frequency, duration):
    t = np.arange(0, duration, 1/sampling_frequency)
    if signal_type == "Sine":
        return t, amplitude * np.sin(2 * np.pi * frequency * t + np.radians(phase_shift))
    elif signal_type == "Cosine":
        return t, amplitude * np.cos(2 * np.pi * frequency * t + np.radians(phase_shift))

def signal_generation_gui():
    gui = Toplevel()
    gui.title("Signal Generation")

    # Continuous or Discrete Representation
    representation_var1 = IntVar()
    representation_var1.set(1)

    representation_var2 = IntVar()
    representation_var2.set(1)

    # Single or Multiple Signals
    representation_var3 = IntVar()
    representation_var3.set(1)

    Radiobutton(gui, text="Single", variable=representation_var3, value=1).grid(row=0, column=0)
    Radiobutton(gui, text="Multiple", variable=representation_var3, value=2).grid(row=0, column=1)
    Radiobutton(gui, text="Continuous", variable=representation_var1, value=1).grid(row=1, column=0)
    Radiobutton(gui, text="Discrete", variable=representation_var1, value=2).grid(row=1, column=1)
    Radiobutton(gui, text="Continuous", variable=representation_var2, value=1).grid(row=8, column=0)
    Radiobutton(gui, text="Discrete", variable=representation_var2, value=2).grid(row=8, column=1)

    # Labels and Entry Fields for Signal 1
    Label(gui, text="Signal 1 Type:").grid(row=2, column=0)
    signal_type_var1 = StringVar(gui)
    signal_type_var1.set("Sine")
    signal_type_dropdown1 = OptionMenu(gui, signal_type_var1, "Sine", "Cosine")
    signal_type_dropdown1.grid(row=2, column=1)

    Label(gui, text="Signal 1 Amplitude (A):").grid(row=3, column=0)
    amplitude1_entry = Entry(gui)
    amplitude1_entry.grid(row=3, column=1)

    Label(gui, text="Signal 1 Phase Shift (θ in degrees):").grid(row=4, column=0)
    phase_shift1_entry = Entry(gui)
    phase_shift1_entry.grid(row=4, column=1)

    Label(gui, text="Signal 1 Frequency (f in Hz):").grid(row=5, column=0)
    frequency1_entry = Entry(gui)
    frequency1_entry.grid(row=5, column=1)

    Label(gui, text="Signal 1 Sampling Frequency (fs in Hz):").grid(row=6, column=0)
    sampling_frequency1_entry = Entry(gui)
    sampling_frequency1_entry.grid(row=6, column=1)

    Label(gui, text="Signal 1 Duration (s):").grid(row=7, column=0)
    duration1_entry = Entry(gui)
    duration1_entry.grid(row=7, column=1)

    # Labels and Entry Fields for Signal 2
    Label(gui, text="Signal 2 Type:").grid(row=9, column=0)
    signal_type_var2 = StringVar(gui)
    signal_type_var2.set("Sine")
    signal_type_dropdown2 = OptionMenu(gui, signal_type_var2, "Sine", "Cosine")
    signal_type_dropdown2.grid(row=9, column=1)

    Label(gui, text="Signal 2 Amplitude (A):").grid(row=10, column=0)
    amplitude2_entry = Entry(gui)
    amplitude2_entry.grid(row=10, column=1)

    Label(gui, text="Signal 2 Phase Shift (θ in degrees):").grid(row=11, column=0)
    phase_shift2_entry = Entry(gui)
    phase_shift2_entry.grid(row=11, column=1)

    Label(gui, text="Signal 2 Frequency (f in Hz):").grid(row=12, column=0)
    frequency2_entry = Entry(gui)
    frequency2_entry.grid(row=12, column=1)

    Label(gui, text="Signal 2 Sampling Frequency (fs in Hz):").grid(row=13, column=0)
    sampling_frequency2_entry = Entry(gui)
    sampling_frequency2_entry.grid(row=13, column=1)

    Label(gui, text="Signal 2 Duration (s):").grid(row=14, column=0)
    duration2_entry = Entry(gui)
    duration2_entry.grid(row=14, column=1)

    def generate_and_plot():
        # Signal 1
        amplitude1 = float(amplitude1_entry.get())
        phase_shift1 = float(phase_shift1_entry.get())
        frequency1 = float(frequency1_entry.get())
        sampling_frequency1 = float(sampling_frequency1_entry.get())
        duration1 = float(duration1_entry.get())
        signal_type1 = signal_type_var1.get()
        
        signal1 = generate_signal(signal_type1, amplitude1, phase_shift1, frequency1, sampling_frequency1, duration1)
        
        # Signal 2
        signal2 = None
        label = None
        multi = False
        if representation_var3.get() == 2:
            amplitude2 = float(amplitude2_entry.get())
            phase_shift2 = float(phase_shift2_entry.get())
            frequency2 = float(frequency2_entry.get())
            sampling_frequency2 = float(sampling_frequency2_entry.get())
            duration2 = float(duration2_entry.get())
            signal_type2 = signal_type_var2.get()
            label = f"Signal 2: {signal_type2} Wave"
            multi = True

            signal2 = generate_signal(signal_type2, amplitude2, phase_shift2, frequency2, sampling_frequency2, duration2)        

        plot_two_signals(signal1, f"Signal 1: {signal_type1} Wave", representation_var1.get(), multi, signal2, label, representation_var2.get())

    generate_button = Button(gui, text="Generate and Plot Signals", command=generate_and_plot)
    generate_button.grid(row=15, columnspan=2)

