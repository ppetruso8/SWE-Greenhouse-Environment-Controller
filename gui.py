'''
Display real time data readings from greenhouse environment, Environment instance
Let user set preferred environmental parameters and pass them to controller

source: https://docs.python.org/3/library/tkinter.html 
        https://realpython.com/python-gui-tkinter/
        https://www.geeksforgeeks.org/python-gui-tkinter/
'''
import tkinter as tk
from tkinter import ttk
from controller import Environment, initialize_sensors, initialize_actuators


class Greenhouse:

   def __init__(self):
      self.temperature = tk.DoubleVar()
      self.humidity = tk.DoubleVar()
      self.light = tk.DoubleVar()


   def read_data(self):
      self.temp_input_label = ttk.Label(root, text="Set Temperature (°C):")
      self.temp_input_label.pack()
      self.temp_entry = ttk.Entry(root)
      self.temp_entry.pack()

      self.humidity_input_label = ttk.Label(root, text="Set Humidity (%):")
      self.humidity_input_label.pack()
      self.humidity_entry = ttk.Entry(root)
      self.humidity_entry.pack()

      self.light_input_label = ttk.Label(root, text="Set Light Spectrum (nm):")
      self.light_input_label.pack()
      self.light_entry = ttk.Entry(root)
      self.light_entry.pack()

      # Button to apply changes
      apply_button = ttk.Button(root, text="Apply Changes", command=Greenhouse.change_environment)
      apply_button.pack()


   def update_readings(self):
      environment = Environment(25.0, 60, 550)
      sensors = initialize_sensors(environment)
      temperature = sensors['temperature'].get_simulator_data()   
      humidity = sensors['humidity'].get_simulator_data()
      light = sensors['light'].get_simulator_data()

      self.current_temperature_label.config(text=f"Temperature: {temperature}°C")
      self.current_humidity_label.config(text=f"Humidity: {humidity}%")
      self.current_light_label.config(text=f"Light: {light}")
      root = tk.Tk()
      root.after(1500, Greenhouse.update_readings)


   def change_environment(self):
       # Get the values from input fields and send commands to actuators
      try:
         self.new_temp = float(Greenhouse.temp_entry.get())
         self.new_humidity = int(Greenhouse.humidity_entry.get())
         self.new_light = int(Greenhouse.light_entry.get())

         environment = Environment(25.0, 60, 550)
         actuators = initialize_actuators(environment)
         actuators['heater'].change_temp(self.new_temp)
         actuators['humidifier'].change_humidity(self.new_humidity)
         actuators['lights'].change_light(self.new_light)
      except ValueError as e:
           print(f"Input error: {e}")


   def setup_gui(self, root):
      # Initialize the Tkinter window
      root = tk.Tk()
      root.title("Greenhouse Environment Controller")

      # Display labels for current environmental readings
      self.current_temperature_label = ttk.Label(root, text="Temperature: --°C")
      self.current_temperature_label.pack()

      self.current_humidity_label = ttk.Label(root, text="Humidity: --%")
      self.current_humidity_label.pack()

      self.current_light_label = ttk.Label(root, text="Light Spectrum: --")
      self.current_light_label.pack()


if __name__ == "__main__":
   root = tk.Tk()
   Greenhouse.setup_gui
   Greenhouse.update_readings
   root.mainloop()


# from controller import Environment
# import tkinter as tk
# from tkinter import ttk
# import random

# class Greenhouse:
#     def __init__(self):
#         self.temperature = tk.DoubleVar()
#         self.humidity = tk.DoubleVar()
#         self.light = tk.DoubleVar()

#     def read_sensor_data(self):
#         #get data from controller 

#         # Environment.set_environment("temperature", 20.0)
#         # Environment.set_environment("humidity", 20.0)
#         # Environment.set_environment("light", 20.0)
#         # self.temperature.set(random.uniform(21, 27))
#         # self.humidity.set(random.uniform(65, 75))
#         # self.light.set(random.uniform(600, 700))

#     def update_data(self):
#         self.read_sensor_data()
#         self.temperature_label.config(text=f"Temperature: {self.temperature.get()} °C")
#         self.humidity_label.config(text=f"Humidity: {self.humidity.get()} %")
#         self.light_label.config(text=f"Light Spectrum: {self.light.get()} nm")

#     def setup_gui(self, root):
#         root.title("Greenhouse Controller")

#         self.temperature_label = ttk.Label(root, text="Temperature: -- °C")
#         self.temperature_label.pack(pady=10)

#         self.humidity_label = ttk.Label(root, text="Humidity: -- %")
#         self.humidity_label.pack(pady=10)

#         self.light_label = ttk.Label(root, text="Light Spectrum: -- nm")
#         self.light_label.pack(pady=10)

#         update_button = ttk.Button(root, text="Update Data", command=self.update_data)
#         update_button.pack(pady=20)


# if __name__ == "__main__":

#     root = tk.Tk()
#     Greenhouse().setup_gui(root)

#     # set up a periodic update of sensor data
#     root.after(500, Greenhouse().update_data)

#     root.mainloop()