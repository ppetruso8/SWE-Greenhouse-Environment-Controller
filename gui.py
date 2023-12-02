'''
Display real time data readings from greenhouse environment, Environment instance
Let user set preferred environmental parameters and pass them to controller

source: https://docs.python.org/3/library/tkinter.html 
        https://realpython.com/python-gui-tkinter/
        https://www.geeksforgeeks.org/python-gui-tkinter/
'''

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



'''
Display real time data readings from greenhouse environment, Environment instance
Let user set preferred environmental parameters and pass them to controller

https://realpython.com/python-gui-tkinter/


from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askinteger

top = Tk()
top.geometry("600x600")

def check():
   msg=messagebox.showinfo( "Check on your environment", "//")

B = Button(top, text ="Check on your environment", command = check)
B.place(x=400,y=500)


# if the environment is optimal then:
var1 = StringVar()
good_message = "the environment is good! :)"
messageVar1 = Message(top, text = good_message)
messageVar1.config(bg='lightgreen')
messageVar1.pack( )

# otherwise:
var2 = StringVar()
bad_message = "the environment is not good! :("
messageVar2 = Message(top, text = bad_message)
messageVar2.config(bg='red')
messageVar2.pack( )




def Lightval():
   light_val = askinteger("Input", "Input the value of Light in your environment")
   #print(light_val)
B = Button(top, text ="Light value", command = Lightval)
B.place(x=300,y=500)


def Humidityval():
   humidity_val = askinteger("Input", "Input the % of Humidity in your environment")
   #print(humidity_val)
B = Button(top, text ="Humidity value", command = Humidityval)
B.place(x=200,y=500)


def Temperatureval():
   temperature_val = askinteger("Input", "Input the temperature in your environment")
   #print(temperature_val)
B = Button(top, text ="Temperature value", command = Temperatureval)
B.place(x=80,y=500)


top.mainloop()
'''