'''
Display real time data readings from greenhouse environment and show appropriate warnings
if current conditions are not ideal.

source: https://docs.python.org/3/library/tkinter.html 
        https://realpython.com/python-gui-tkinter/
        https://www.geeksforgeeks.org/python-gui-tkinter/
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

   warning_label = ttk.Label(root, text="Environment is in ideal condition")
   warning_label.pack()

   warning_label_temperature = ttk.Label(root, text="The temperature level is good")
   warning_label_temperature.pack()

   warning_label_humidity = ttk.Label(root, text="The humidity level is good")
   warning_label_humidity.pack()

   warning_label_light = ttk.Label(root, text="The light brightness is good")
   warning_label_light.pack()


   return root, current_temperature_label, current_humidity_label, current_light_label, warning_label, warning_label_temperature, warning_label_humidity, warning_label_light


def update_gui(current_temperature_label, current_humidity_label, current_light_label, temperature, humidity, light):
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


def display_warning(warning_label_temperature, variable, warning):
   ''' Display warning
   '''
   if variable == "temperature":
      if warning == "high":
         warning_label_temperature.config(text=f"Warning: the temperature is too high\n")
      elif variable == "low": 
         warning_label_temperature.config(text=f"Warning: the temperature is too low\n")
      # else:
      #    warning_label_temperature.config(text=f"the temperature is good\n") #(?)

   if variable == "humidity":
      if warning == "high":
         warning_label.config(text=f"Warning: the humidity is too high\n")
      else: 
         warning_label.config(text=f"Warning: the humidity is too low\n")

   if variable == "light":
      if warning == "high":
         warning_label = Label(text="Warning: the light is too bright\n", bg="red")
         warning_label.pack(pady=10)

      else: 
         warning_label = Label(text="Warning: the light is too dark\n", bg="red")
         warning_label.pack(pady=10)
