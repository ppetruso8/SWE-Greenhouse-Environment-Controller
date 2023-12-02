'''
Display real time data readings from greenhouse environment, Environment instance
Let user set preferred environmental parameters and pass them to controller

source: https://docs.python.org/3/library/tkinter.html 
        https://realpython.com/python-gui-tkinter/
        https://www.geeksforgeeks.org/python-gui-tkinter/
'''

import tkinter as tk
from tkinter import ttk

def initialize_gui():
   root = tk.Tk()
   root.title("Greenhouse Environment Controller")

   current_temperature_label = ttk.Label(root, text="Temperature: --°C")
   current_temperature_label.pack()

   current_humidity_label = ttk.Label(root, text="Humidity: --%")
   current_humidity_label.pack()

   current_light_label = ttk.Label(root, text="Light Spectrum: --nm")
   current_light_label.pack()

   return root, current_temperature_label, current_humidity_label, current_light_label

def update_gui(current_temperature_label, current_humidity_label, current_light_label, temperature, humidity, light):
   current_temperature_label.config(text=f"Temperature: {temperature}°C")
   current_humidity_label.config(text=f"Humidity: {humidity}%")
   current_light_label.config(text=f"Light Spectrum: {light}nm")