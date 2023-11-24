''' 
Main Greenhouse Environment Controller code.
Responsible for launching UI, processing data, and adjusting actuators
'''

from sensors import initialize_sensors

class Environment():
    '''
    Class representing environment
    '''
    def __init__(self, temp: float, humidity: int, light: int):
        self.environment = {
            "temperature": temp,
            "humidity": humidity,
            "light": light
        }

    # change environment state
    def set_environment(self, variable: str, value):
        '''
        variable -- environment variable
        value -- value to update the variable
        '''
        if variable in self.environment:
            self.environment[variable] = value
        else:
            raise ValueError("Invalid environment variable %s", variable)
    
    # get current environment state
    def get_environment(self):
        return self.environment
    
    # get current environment variable state
    def get_environment(self, variable: str):
        '''
        variable -- name of the environment variable
        '''
        return self.environment[variable]

def main():
    # create environment
    environment = Environment(25.0,60,550)

    # from actuators.py
    # initialize_actuators()

    # from gui.py
    #launch_gui()
    
    # main loop 
    work(environment)

def work(env):
    #while True:
    # get sensors in dictionary
    sensors = initialize_sensors()
    temperature_data = sensors["temperature"].get_data(env)
    humidity_data = sensors["humidity"].get_data(env)
    light_data = sensors["light"].get_data(env)
    print(temperature_data, humidity_data, light_data)
    

if __name__ == "__main__":
    main()