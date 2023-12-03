''' 
Main Greenhouse Environment Controller code.
Responsible for initializing the greenhouse environment, sensors, actuators, GUI,
and managing the main loop for controlling the system.
'''

from sensors import TemperatureSensor, LightSensor, HumiditySensor
from actuators import Heater, Humidifier, Lights
from gui import update_gui, initialize_gui, display_warning
from time import sleep

class Environment():
    ''' Class representing the greenhouse environment

    Attributes:
    environment -- dictionary storing temperature, humidity and light values
    ideal_condition -- dictionary storing ideal environment conditions
    '''
    def __init__(self, temp: float, humidity: int, light: int):
        ''' Initialize environment with values given in from parameters

        Create 2 dictionaries: 
            environment -- current environment state
            ideal_condition -- ideal condition state for environment

        temp -- initial temperature of environment
        humidity -- initial humidity of environment
        light -- initial light spectrum of environment
        '''
        self.environment = {
            "temperature": temp,
            "humidity": humidity,
            "light": light
        }
        
        self.ideal_condition = {
            "temp_upper": 27.0,
            "temp_lower": 21.0,
            "humidity_upper": 80,
            "humidity_lower": 65,
            "light_upper": 700,
            "light_lower": 600
        }

    def set_environment(self, variable: str, value):
        ''' Update the value of a specific environmental variable

        variable -- environment variable
        value -- value to update the variable
        '''
        if type(variable) != str:
            raise TypeError("Environment variable must be passed in as a string")

        if variable in self.environment:
            if variable == "temperature":
                if value > 40.0:
                    raise ValueError("Maximum allowed temperature is 40.0°C")
                elif value < 15.0:
                    raise ValueError("Minimum allowed temperature is 15.0°C")
            elif variable == "humidity":
                if value > 100:
                    raise ValueError("Maximum allowed humidity is 100%")
                elif value < 40:
                    raise ValueError("Minimum allowed humidity is 40%")
            elif variable == "light":
                if value > 850:
                    raise ValueError("Maximum allowed light spectrum value is 850nm")
                elif value < 150:
                    raise ValueError("Minimum allowed light spectrum value is 150nm")

            self.environment[variable] = value
        else:
            raise ValueError("Invalid environment variable: %s" % variable)
    
    def get_environment(self):
        ''' Get the current state of the environment
        '''
        return self.environment
    
    def get_environment_variable(self, variable: str):
        ''' Get the current value of a specific environmental variable

        variable -- name of the environment variable
        '''
        if type(variable) != str:
            raise TypeError("Environment variable must be passed in as a string")

        if variable in self.environment:
            return self.environment[variable]
        else:
            raise ValueError("Invalid environment variable: %s" % variable)
        
    def get_ideal_conditions(self):
        ''' Return dictionary containing ideal condition of environment
        '''
        return self.ideal_condition

def main():
    ''' Main function to create environment and initialize sensors, actuators, GUI and to start the main control loop
    '''
    # create environment
    environment = Environment(25.0,60,550)

    # initialize sensors and actuators
    sensors = initialize_sensors(environment)
    actuators = initialize_actuators(environment)

    # initialize gui and put gui data into dictionary
    root, temp_label, humidity_label, light_label, warning_label_temperature, warning_label_humidity, warning_label_light = initialize_gui()
    gui = {"root": root, "temp_label": temp_label, "humidity_label": humidity_label, "light_label": light_label, "warning_label_temperature": warning_label_temperature, "warning_label_humidity": warning_label_humidity, "warning_label_light": warning_label_light}
        
    # main control loop 
    work(environment, sensors, actuators, gui)

def work(env, sensors: dict, actuators: dict, gui: dict, i: int = -1):
    ''' Main control loop to simulate greenhouse environment controller

    In the while loop, the controller continually fetches data about the environment
    from the sensors, and displays them through GUI. 
    If any of the environment condition is not ideal, it will generate a warning that 
    would be displayed to user through GUI and it will try to get back to the ideal state.

    Can operate in test mode, so that there is a set number of iterations - this
    is triggered by setting the value of test to >0

    env -- greenhouse environment instance
    sensors -- dictionary of sensors
    actuators -- dictionary of actuators
    gui -- dictionary containing root of gui and labels for environmental variables
    i -- determine the number of iterations for while loop
        default: -1 (infinite while loop)
    '''
    while (i+1) != True:
        # fetch data from sensors
        temperature_data = sensors["temperature"].get_simulator_data()
        humidity_data = sensors["humidity"].get_simulator_data()
        light_data = sensors["light"].get_simulator_data()
        
        # send environment data to GUI
        gui["root"].after(0, update_gui, gui["temp_label"], gui["humidity_label"], gui["light_label"], 
                   temperature_data, humidity_data, light_data)

        # get ideal environment condition
        ideal_conditions = env.get_ideal_conditions()

        # send warning if environment status not ideal and activate actuators
        if temperature_data > ideal_conditions["temp_upper"] or temperature_data < ideal_conditions["temp_lower"]:
            if temperature_data > ideal_conditions["temp_upper"]:
                display_warning(gui["warning_label_temperature"],"temperature", "high")
                actuators["heater"].change_temp(ideal_conditions["temp_upper"])
            else:
                display_warning(gui["warning_label_temperature"], "temperature", "low")
                actuators["heater"].change_temp(ideal_conditions["temp_lower"])

        else:
            display_warning(gui["warning_label_temperature"], "temperature", "good")

        if humidity_data > ideal_conditions["humidity_upper"] or humidity_data < ideal_conditions["humidity_lower"]:
            if humidity_data > ideal_conditions["humidity_upper"]:
                display_warning(gui["warning_label_humidity"], "humidity", "high")
                actuators["humidifier"].change_humidity(ideal_conditions["humidity_upper"])
            else:
                display_warning(gui["warning_label_humidity"], "humidity", "low")
                actuators["humidifier"].change_humidity(ideal_conditions["humidity_lower"])

        else: 
            display_warning(gui["warning_label_humidity"], "humidity", "good")

        if light_data > ideal_conditions["light_upper"] or light_data < ideal_conditions["light_lower"]:
            if light_data > ideal_conditions["light_upper"]:
                display_warning(gui["warning_label_light"], "light", "high")
                actuators["lights"].change_light(ideal_conditions["light_upper"])
            else:
                display_warning(gui["warning_label_light"], "light", "low")
                actuators["lights"].change_light(ideal_conditions["light_lower"])

        else: 
            display_warning(gui["warning_label_light"], "light", "good")

        # update gui
        gui["root"].update()

        # decrement i to continue while loop
        i -= 1

        # wait for 2 seconds before next loop
        sleep(2)

def initialize_sensors(environment):
    ''' Create an instance of each sensor and return dictionary of sensor objects
    
    environment -- environment instance
    '''
    temperature_sensor = TemperatureSensor(environment)
    humidity_sensor = HumiditySensor(environment)
    light_sensor = LightSensor(environment)
    
    sensors = {"temperature": temperature_sensor, "humidity": humidity_sensor, "light": light_sensor}

    return sensors

def initialize_actuators(environment):
    ''' Create an instance of each actuator and return dictionary of actuator objects
    
    environment -- environment instance
    '''
    heater = Heater(environment)
    humidifier = Humidifier(environment)
    lights = Lights(environment)
    
    # put actuators into the output dictionary
    actuators = {"heater": heater, "humidifier": humidifier, "lights": lights}

    return actuators
    
if __name__ == "__main__":
    main()