''' 
Main Greenhouse Environment Controller code.
Responsible for initializing the greenhouse environment, sensors, actuators, GUI,
and managing the main loop for controlling the system.
'''

from sensors import initialize_sensors
from actuators import initialize_actuators

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
    #while True:
    
    # temporary for loop to simulate environment
    i = 0
    try:
        for i in range(20):
            # get sensors in dictionary
            temperature_data = sensors["temperature"].get_simulator_data()
            humidity_data = sensors["humidity"].get_simulator_data()
            light_data = sensors["light"].get_simulator_data()

            print(temperature_data, humidity_data, light_data)

            i += 1
    except Exception as e:
        print("An error has ocurred in main control loop: %s" % e)
    
if __name__ == "__main__":
    main()