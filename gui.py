'''
Display real time data readings from greenhouse environment
Option 1: let user set preferred environmental parameters
Option 2: Raise warnings when environment condition not optimal and solve
tkinter?
'''
import tkinter as tk
from tkinter import ttk

# Import your modules here
from app import Environment, initialize_sensors, initialize_actuators

# Initialize environment, sensors, and actuators
environment = Environment(25.0, 60, 550)
sensors = initialize_sensors(environment)
actuators = initialize_actuators(environment)

def update_readings():
    # Update the GUI with the latest sensor readings
    temperature = sensors['temperature'].get_simulator_data()
    humidity = sensors['humidity'].get_simulator_data()
    light = sensors['light'].get_simulator_data()

    current_temperature_label.config(text=f"Temperature: {temperature}°C")
    current_humidity_label.config(text=f"Humidity: {humidity}%")
    current_light_label.config(text=f"Light: {light}")

    root.after(1000, update_readings)

def change_environment():
    # Get the values from input fields and send commands to actuators
    try:
        new_temp = float(temp_entry.get())
        new_humidity = int(humidity_entry.get())
        new_light = int(light_entry.get())

        actuators['heater'].change_temp(new_temp)
        actuators['humidifier'].change_humidity(new_humidity)
        actuators['lights'].change_light(new_light)
    except ValueError as e:
        print(f"Input error: {e}")

# Initialize the Tkinter window
root = tk.Tk()
root.title("Greenhouse Environment Controller")

# Display labels for current environmental readings
current_temperature_label = ttk.Label(root, text="Temperature: --°C")
current_temperature_label.pack()

current_humidity_label = ttk.Label(root, text="Humidity: --%")
current_humidity_label.pack()

current_light_label = ttk.Label(root, text="Light: --")
current_light_label.pack()

# Entry fields with descriptive labels for user input
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

# Button to apply changes
apply_button = ttk.Button(root, text="Apply Changes", command=change_environment)
apply_button.pack()

# Start the update loop
update_readings()

# Run the application
root.mainloop()
