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
    '''
    def __init__(self, temp: float, humidity: int, light: int):
        ''' Initialize environment with values given in from parameters

        Create 2 dictionaries: 
            environment -- current environment state
            user_setting -- desired environment state after user requests change in environment parameters in GUI

        temp -- initial temperature of environment
        humidity -- initial humidity of environment
        light -- initial light spectrum of environment
        '''
        if type(temp) == int:
            temp = float(temp)
        elif type(temp) != float:
            raise TypeError("Temperature of environment must be passed in as a float")
        
        if type(humidity) != int:
            raise TypeError("Humidity of environment must be passed in as an integer")
        
        if type(light) != int:
            raise TypeError("Light spectrum value of environment must be passed in as an integer")

        self.environment = {
            "temperature": temp,
            "humidity": humidity,
            "light": light
        }
        
        self.user_setting = {
            "user_temp": None,
            "user_humidity": None,
            "user_light": None
        }

    def set_environment(self, variable: str, value):
        ''' Update the value of a specific environmental variable

        variable -- environment variable
        value -- value to update the variable
        '''
        if type(variable) != str:
            raise TypeError("Environment variable must be passed in as a string")

        if variable in self.environment:
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
        
    def set_user_settings(self, temperature: float = None, humidity: int = None, light: int = None):
        ''' Update user setting for environment

        temperature -- user input value for temperature
            default: None
        humidity -- user input value for humidity
            default: None
        light -- user input value for light spectrum
            default: None
        '''
        if temperature != None:
            if type(temperature) == int:
                temperature = float(temperature)

            if type(temperature) != float:
                raise TypeError("Temperature must be passed in as a float")
            else:
                self.user_setting["user_temp"] = temperature
        
        if humidity != None:
            if type(humidity) != int:
                raise TypeError("Humidity must be passed in as an integer")
            else:
                self.user_setting["user_humidity"] = humidity
        
        if light != None:
            if type(light) != int:
                raise TypeError("Light spectrum value must be passed in as an integer")
            else:
                self.user_setting["user_light"] = light

    def get_user_setting(self):
        ''' Return dictionary containing user setting
        '''
        return self.user_setting

def main():
    ''' Main function to create environment and initialize sensors, actuators, GUI and to start the main control loop
    '''
    try:
        # create environment
        environment = Environment(25.0,60,550)

        # initialize sensors and actuators
        sensors = initialize_sensors(environment)
        actuators = initialize_actuators(environment)

        # initialize_gui(environment)
        
        # main control loop 
        work(environment, sensors, actuators)
    except Exception as e:
        print("An error has ocurred in main: %s" % e)

def work(env, sensors: dict, actuators: dict, test: int = 0):
    ''' Main control loop to simulate greenhouse environment

    In the while loop, the controller continually fetches data about the environment
    from the sensors, displays them through GUI. 
    It also checks for the possible user input from GUI and based on it calls to
    appropriate actuator to change the environment appropriately if there is a
    difference between values of current environment variables and those passed
    from a user. 
    To activate an actuator, there must be a difference for each variable:
        - temperature: difference of more than 1°C
        - humidity: difference of more than 2%
        - lights: difference of more than 5nm

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
    try:
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
            
            # # check for user input
            # get_user_input(env)

            # get user settings
            user_settings = env.get_user_setting()

            # check for values in user settings and activate actuator if necessary
            if user_settings["user_temp"] != None:
                temp_difference = abs(temperature_data - user_settings["user_temp"])

                if temp_difference > 1:      
                    actuators["heater"].change_temp(user_settings["user_temp"])

            if user_settings["user_humidity"] != None:
                humidity_difference = abs(humidity_data - user_settings["user_humidity"])

                if humidity_difference > 2:
                    actuators["humidifier"].change_humidity(user_settings["user_humidity"])

            if user_settings["user_light"] != None:
                light_difference = abs(light_data - user_settings["user_light"])

                if light_difference > 5:
                    actuators["lights"].change_light(user_settings["user_light"])

            # update_gui()

            # test loop control
            if i > 0 and i >= test:
                break

            if test > 0:
                i += 1

            #DELETE THIS AFTER REMOVING FOR LOOP
            temp_i += 1

    except Exception as e:
        print("An error has ocurred in main control loop: %s" % e)

# def get_user_input(env):
''' Get user input from GUI
'''
#   ... code for getting user input from gui ...
#   if temp set in GUI:
#       user_temp = ....
#       env.set_user_setting(temperature = user_temp)
#   
#   if humidity set in GUI:
#       user_humidity = ....
#       env.set_user_setting(humidity = user_humidity)
#   
#   if light set in GUI:
#       user_light = ....
#       env.set_user_setting(light = user_light)


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
    
if __name__ == "__main__":
    main()