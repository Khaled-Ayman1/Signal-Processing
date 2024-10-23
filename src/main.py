import tkinter as tk
from signal_processing import signal_processing_gui
from signal_generation import signal_generation_gui

def main_menu():
    main_root = tk.Tk()
    main_root.title("Main Menu")

    def launch_task_1():
        main_root.destroy()
        signal_processing_gui()
    
    def launch_task_2():
        main_root.destroy()
        signal_generation_gui()

    task_1_button = tk.Button(main_root, text="Task 1: Signal Processing", command=launch_task_1)
    task_1_button.pack(pady=20)

    task_2_button = tk.Button(main_root, text="Task 2: Signal Generation", command=launch_task_2)
    task_2_button.pack(pady=20)

    main_root.mainloop()
if __name__ == "__main__":
    main_menu()