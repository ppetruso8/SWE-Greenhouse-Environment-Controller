''' 
Main Greenhouse Environment Controller code.
Responsible for initializing the greenhouse environment, sensors, actuators, GUI,
and managing the main loop for controlling the system.
'''

from sensors import TemperatureSensor, LightSensor, HumiditySensor
from actuators import Heater, Humidifier, Lights
# from gui import update_gui, initialize_gui

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
    try:
        # create environment
        environment = Environment(25.0,60,550)

        # initialize sensors and actuators
        sensors = initialize_sensors(environment)
        actuators = initialize_actuators(environment)

        # initialize_gui(environment)?
        
        # main control loop 
        work(environment, sensors, actuators)
    except Exception as e:
        print("An error has ocurred in main: %s" % e)

def work(env, sensors: dict, actuators: dict, test: int = 0):
    ''' Main control loop to simulate greenhouse environment

    In the while loop, the controller continually fetches data about the environment
    from the sensors, and displays them through GUI. 
    If any of the environment condition is not ideal, it will generate a warning that 
    would be displayed to user through GUI and it will try to get back to the ideal state.

    Can operate in test mode, so that there is a set number of iterations - this
    is triggered by setting the value of test to >0

    env -- greenhouse environment instance
    sensors -- dictionary of sensors
    actuators -- dictionary of actuators
    test -- determine if this function call is for testing purpose
        default: 0
    '''
    i = 0

    # DELETE THIS AFTER REMOVING FOR LOOP
    temp_i = 0
    # while True:
    for temp_i in range(20):
        # get sensor data from simulator if not testing
        if test == 0:
            temperature_data = sensors["temperature"].get_simulator_data()
            humidity_data = sensors["humidity"].get_simulator_data()
            light_data = sensors["light"].get_simulator_data()
        else:
            temperature_data = sensors["temperature"].get_environment_data(env)
            humidity_data = sensors["humidity"].get_environment_data(env)
            light_data = sensors["light"].get_environment_data(env)

        print(temperature_data, humidity_data, light_data)

        # send environment data to GUI
        # update_gui()

        check_ideal_conditions(temperature_data, humidity_data, light_data, env, actuators)

        if test > 0:
            i += 1

        # test loop control
        if i > 0 and i >= test:
            break

        #DELETE THIS AFTER REMOVING FOR LOOP
        temp_i += 1 

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
    heater = Heater(environment)
    humidifier = Humidifier(environment)
    lights = Lights(environment)
    
    # put actuators into the output dictionary
    actuators = {"heater": heater, "humidifier": humidifier, "lights": lights}

    return actuators

def check_ideal_conditions(temp, humidity, light, env, actuators):
    ''' Check whether the current environment conditions are ideal

    If current conditions are not ideal, sends warning to the GUI and activates
    appropriate actuator

    temp -- current temperature of an environment
    humidity -- current humidity of an environment
    light -- current light spectrum value of an environment
    env -- environment instance variable
    actuators -- dictionary containing current environment actuators
    '''
    # get ideal environment condition
    ideal_conditions = env.get_ideal_conditions()
    # send warning if environment status not ideal and activate actuators
    if temp > ideal_conditions["temp_upper"]:
        #send_high_temperature_warning()
        actuators["heater"].change_temp(ideal_conditions["temp_upper"])
    elif temp < ideal_conditions["temp_lower"]:
        #send_low_temperature_warning()
        actuators["heater"].change_temp(ideal_conditions["temp_lower"])

    if humidity > ideal_conditions["humidity_upper"]:
        #send_high_humidity_warning()
        actuators["humidifier"].change_humidity(ideal_conditions["humidity_upper"])
    elif humidity < ideal_conditions["humidity_lower"]:
        #send_low_temperature_warning()
        actuators["humidifier"].change_humidity(ideal_conditions["humidity_lower"])

    if light > ideal_conditions["light_upper"]:
        #send_strong_light_warning()
        actuators["lights"].change_light(ideal_conditions["light_upper"])
    elif light < ideal_conditions["light_lower"]:
        #send_weak_light_warning()
        actuators["lights"].change_light(ideal_conditions["light_lower"])
    
if __name__ == "__main__":
    main()