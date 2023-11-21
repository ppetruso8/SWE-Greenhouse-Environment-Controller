'''
tkinter? display real time data, let user set preferred environmental parameters
source: https://docs.python.org/3/library/tkinter.html 
        https://realpython.com/python-gui-tkinter/
        https://www.geeksforgeeks.org/python-gui-tkinter/
'''
import tkinter as tk
from tkinter import ttk
import random

class GreenhouseController:
    def __init__(self):
        self.temperature = tk.DoubleVar()
        self.humidity = tk.DoubleVar()
        self.light = tk.DoubleVar()

    def read_sensor_data(self):
        self.temperature.set(random.uniform(21, 27))
        self.humidity.set(random.uniform(65, 75))
        self.light.set(random.uniform(600, 700))

    def update_data(self):
        self.read_sensor_data()
        self.temperature_label.config(text=f"Temperature: {self.temperature.get()} °C")
        self.humidity_label.config(text=f"Humidity: {self.humidity.get()} %")
        self.light_label.config(text=f"Light Spectrum: {self.light.get()} nm")

    def setup_gui(self, root):
        root.title("Greenhouse Controller")

        self.temperature_label = ttk.Label(root, text="Temperature: -- °C")
        self.temperature_label.pack(pady=10)

        self.humidity_label = ttk.Label(root, text="Humidity: -- %")
        self.humidity_label.pack(pady=10)

        self.light_label = ttk.Label(root, text="Light Spectrum: -- nm")
        self.light_label.pack(pady=10)

        update_button = ttk.Button(root, text="Update Data", command=self.update_data)
        update_button.pack(pady=20)

        quit_button = ttk.Button(root, text="Quit", command=root.destroy)
        quit_button.pack(pady=20)

if __name__ == "__main__":
    greenhouse = GreenhouseController()

    root = tk.Tk()
    greenhouse.setup_gui(root)

    # set up a periodic update of sensor data (?)
    root.after(5000, greenhouse.update_data)

    root.mainloop()