''' 
Main Greenhouse Environment Controller code.
Responsible for initializing the greenhouse environment, sensors, actuators, GUI,
and managing the main loop for controlling the system.
After user requests to change the environment state, controller is responsible for
managing actuators and maintenance of the final state.
'''

from sensors import TemperatureSensor, HumiditySensor, LightSensor
from actuators import Heater, Humidifier, Lights

class Environment():
    ''' Class representing the greenhouse environment

    Attributes:
    environment -- dictionary storing temperature, humidity and light values
    '''
    def __init__(self, temp: float, humidity: int, light: int):
        ''' Initialize environment with values given in from parameters

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
        if variable in self.environment:
            return self.environment[variable]
        else:
            raise ValueError("Invalid environment variable: %s" % variable)
        
def get_user_input():
    # code for getting the user input from GUI
    # if user_input:
    #   return user_input
    # else:
    #   return None
    pass

def main():
    ''' Main function to create environment and initialize sensors, actuators, GUI and to start the main control loop
    '''
    try:
        # create environment
        environment = Environment(25.0,60,550)

        # initialize sensors and actuators
        sensors = initialize_sensors(environment)
        actuators = initialize_actuators(environment)

        # from gui.py
        #launch_gui()
        
        # main control loop 
        work(environment, sensors, actuators)
    except Exception as e:
        print("An error has ocurred in main: %s" % e)

def work(env, sensors: dict, actuators: dict):
    ''' Main control loop to simulate greenhouse environment

    env -- greenhouse environment instance
    sensors -- dictionary of sensors
    actuators -- dictionary of actuators
    '''
    # temporary for loop to simulate environment
    i = 0
    try:
        #while True:
        for i in range(20):
            # get sensors in dictionary
            temperature_data = sensors["temperature"].get_simulator_data()
            humidity_data = sensors["humidity"].get_simulator_data()
            light_data = sensors["light"].get_simulator_data()

            print(temperature_data, humidity_data, light_data)

            # user_input = get_user_input()

            # change environment variables to user setting and maintain the state
            # if user_input != None:
            #   actuators["heater"].change_temp(user_input[0])
            #   actuators["humidifier"].change_humidity(user_input[1])
            #   actuators["light"].change_light(user_input[2])

            i += 1
    except Exception as e:
        print("An error has ocurred in main control loop: %s" % e)

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