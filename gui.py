'''
Display real time data readings from greenhouse environment and show appropriate warnings
if current conditions are not ideal.
'''
from tkinter import *
import tkinter as tk
from tkinter import ttk


def initialize_gui():
    '''Create GUI window for the greenhouse environment controller with labels for environment variables
    '''
    # create main window
    root = tk.Tk()
    # set the window's title
    root.title("Greenhouse Environment Controller")
    # set the size of the window
    root.geometry("700x350")

    # create and pack labels for environment variables
    current_temperature_label = ttk.Label(root, text="Temperature: --°C")
    current_temperature_label.pack()

    current_humidity_label = ttk.Label(root, text="Humidity: --%")
    current_humidity_label.pack()

    current_light_label = ttk.Label(root, text="Light Spectrum: --nm")
    current_light_label.pack()

    warning_label_temperature = ttk.Label(root, text="")
    warning_label_temperature.pack()

    warning_label_humidity = ttk.Label(root, text="")
    warning_label_humidity.pack()

    warning_label_light = ttk.Label(root, text="")
    warning_label_light.pack()

    gui = {"root": root, "temp_label": current_temperature_label, "humidity_label": current_humidity_label, 
           "light_label": current_light_label, "warning_label_temperature": warning_label_temperature, 
           "warning_label_humidity": warning_label_humidity, "warning_label_light": warning_label_light}

    return gui


def update_gui(current_temperature_label, current_humidity_label, current_light_label, temperature: float, humidity: int, light: int):
   '''Update GUI labels with the current environment data
   
   current_temperature_label -- label for displaying temperature 
   current_humidity_label -- label for displaying humidity
   current-light-label -- label for displaying light spectrum 
   temperature -- current temperature in the greenhouse
   humidity -- current humidity in the greenhouse
   light -- current light spectrum value in the greenhouse
   '''
   current_temperature_label.config(text=f"Temperature: {temperature} °C")
   current_humidity_label.config(text=f"Humidity: {humidity} %")
   current_light_label.config(text=f"Light Spectrum: {light} nm")


def display_warning(warning_label, variable: str, warning: str):
    ''' Display warning message when current environment state is not ideal

    warning_label -- tkinter Label for displaying the warning message
    variable -- name of the variable that is not in ideal state
    warning -- type of the warning that should be displayed
    '''
    if variable == "temperature":
        if warning == "high":
            warning_label.config(text=f"Warning: the temperature is too high\n")
        elif warning == "low": 
            warning_label.config(text=f"Warning: the temperature is too low\n")
        else:
            warning_label.config(text=f"")

    elif variable == "humidity":
        if warning == "high":
            warning_label.config(text=f"Warning: the humidity is too high\n")
        elif warning == "low":
            warning_label.config(text=f"Warning: the humidity is too low\n")
        else:
            warning_label.config(text=f"")

    elif variable == "light":
        if warning == "high":
            warning_label.config(text=f"Warning: the light is too strong\n")
        elif warning == "low":
            warning_label.config(text=f"Warning: the light is too weak\n")
        else:
            warning_label.config(text=f"")

    else:
        raise ValueError("Invalid environment variable: %s" % variable)
