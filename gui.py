'''
Display real time data readings from greenhouse environment and show appropriate warnings
if current conditions are not ideal.

source: https://docs.python.org/3/library/tkinter.html 
        https://realpython.com/python-gui-tkinter/
        https://www.geeksforgeeks.org/python-gui-tkinter/
'''

import tkinter as tk
from tkinter import ttk

def initialize_gui():
   '''Create GUI window for the greenhouse environment controller with labels for environment variables
   '''
   # create main window
   root = tk.Tk()
   # set the window's title
   root.title("Greenhouse Environment Controller")

   # create and pack labels for environment variables
   current_temperature_label = ttk.Label(root, text="Temperature: --°C")
   current_temperature_label.pack()

   current_humidity_label = ttk.Label(root, text="Humidity: --%")
   current_humidity_label.pack()

   current_light_label = ttk.Label(root, text="Light Spectrum: --nm")
   current_light_label.pack()

   warning_label = ttk.Label(root, text="Environment is in ideal condition")
   warning_label.pack()

   return root, current_temperature_label, current_humidity_label, current_light_label, warning_label

def update_gui(current_temperature_label, current_humidity_label, current_light_label, temperature, humidity, light):
   '''Update GUI labels with the current environment data
   
   current_temperature_label -- label for displaying temperature 
   current_humidity_label -- label for displaying humidity
   current-light-label -- label for displaying light spectrum 
   temperature -- current temperature in the greenhouse
   humidity -- current humidity in the greenhouse
   light -- current light spectrum value in the greenhouse
   '''
   current_temperature_label.config(text=f"Temperature: {temperature}°C")
   current_humidity_label.config(text=f"Humidity: {humidity}%")
   current_light_label.config(text=f"Light Spectrum: {light}nm")

def display_warning(warning_label, variable, warning):
   ''' Display warning
   
   '''
   # if variable is "temperature"
   #   if warning is "high"
   #        warning_label.config(text=f"Warning: the temperature is too high")
   #   if warning is "low"
   #        warning_label.config(text=f"Warning: the temperature is too low")
   #... etc for each variable