'''
Module containing sensors classes for temperature, humidity and light sensors.

Each sensor class is able to fetch data from simulator or environment that can be then 
used by controller to process further.
'''

import simulator

class TemperatureSensor:
    ''' Sensor class for sensing the temperature in the environment 

    Ideal temperature of the environment should be between 21°C and 27°C.

    Attributes:
    env -- environment instance representing current environment
    '''
    def __init__(self, environment):
        ''' Initialize the sensor
        
        environment -- environment instance
        '''
        self.env = environment

    def get_simulator_data(self):
        ''' Fetch current environment temperature data from simulator
        '''
        try:
            return simulator.get_simulator_data("temperature", self.env)
        except Exception as e:
            print("Error fetching temperature data from simulator: %s" % e)
            return None
    
    # get environment data from environment class instance
    def get_environment_data(self, environment):
       ''' Fetch current environment temperature data directly from environment

       environment -- environment instance
       '''
       try:
            return environment.get_environment_variable("temperature")
       except Exception as e:
            print("Error fetching temperature data from environment: %s" % e)
            return None

class HumiditySensor:
    ''' Sensor class for sensing the temperature in the environment 

    Ideal humidity of the environment should be 65 - 75% during the night and 80% during the day.

    Attributes:
    env -- environment instance representing current environment
    '''
    def __init__(self, environment):
        ''' Initialize the sensor
        
        environment -- environment instance
        '''
        self.env = environment

    def get_simulator_data(self):
        ''' Fetch current environment humidity data from simulator
        '''
        try:
            return simulator.get_simulator_data("humidity", self.env)
        except Exception as e:
            print("Error fetching humidity data from simulator: %s" % e)
            return None
    
    def get_environment_data(self, environment):
       ''' Fetch current environment humidity data directly from environment

       environment -- environment instance
       '''
       try:
            return environment.get_environment_variable("humidity")
       except Exception as e:
            print("Error fetching humidity data from environment: %s" % e)
            return None

class LightSensor:
    ''' Sensor class for sensing the temperature in the environment 

    Ideal light spectrum of the environment should be between 600nm and 700nm.

    Attributes:
    env -- environment instance representing current environment
    '''
    def __init__(self, environment):
        ''' Initialize the sensor
        
        environment -- environment instance
        '''
        self.env = environment

    def get_simulator_data(self):
        ''' Fetch current light spectrum data from simulator
        '''
        try:
            return simulator.get_simulator_data("light", self.env)
        except Exception as e:
            print("Error fetching light spectrum data from simulator: %s" % e)
            return None
    
    def get_environment_data(self, environment):
       ''' Fetch current environment light spectrum data directly from environment

       environment -- environment instance
       '''
       try:
            return environment.get_environment_variable("light")
       except Exception as e:
            print("Error fetching light spectrum data from environment: %s" % e)
            return None