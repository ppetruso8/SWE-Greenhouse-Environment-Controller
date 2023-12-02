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


environment = Environment(25.0, 60, 550)
sensors = initialize_sensors(environment)
actuators = initialize_actuators(environment)

def update_readings():
    temperature = sensors['temperature'].get_simulator_data()
    humidity = sensors['humidity'].get_simulator_data()
    light = sensors['light'].get_simulator_data()

    current_temperature_label.config(text=f"Temperature: {temperature}°C")
    current_humidity_label.config(text=f"Humidity: {humidity}%")
    current_light_label.config(text=f"Light: {light}")

    root.after(1500, update_readings)

def change_environment():
    try:
        new_temp = float(temp_entry.get())
        new_humidity = int(humidity_entry.get())
        new_light = int(light_entry.get())

        actuators['heater'].change_temp(new_temp)
        actuators['humidifier'].change_humidity(new_humidity)
        actuators['lights'].change_light(new_light)
    except ValueError as e:
        print(f"Input error: {e}")

root = tk.Tk()
root.title("Greenhouse Environment Controller")


current_temperature_label = ttk.Label(root, text="Temperature: --°C")
current_temperature_label.pack()

current_humidity_label = ttk.Label(root, text="Humidity: --%")
current_humidity_label.pack()

current_light_label = ttk.Label(root, text="Light: --")
current_light_label.pack()


temp_input_label = ttk.Label(root, text="Set Temperature (°C):")
temp_input_label.pack()
temp_entry = ttk.Entry(root)
temp_entry.pack()

humidity_input_label = ttk.Label(root, text="Set Humidity (%):")
humidity_input_label.pack()
humidity_entry = ttk.Entry(root)
humidity_entry.pack()

light_input_label = ttk.Label(root, text="Set Light (value):")
light_input_label.pack()
light_entry = ttk.Entry(root)
light_entry.pack()


apply_button = ttk.Button(root, text="Apply Changes", command=change_environment)
apply_button.pack()

# Start the update loop
update_readings()

# Run the application
root.mainloop()