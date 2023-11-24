'''
Module containing sensors classes.
Sensors get data from simulator, process them and send data to the controller.
'''

import simulator

class TemperatureSensor:
    # ideal temperature between 21 to 27°C
    def __init__(self, environment):
        self.env = environment
    # get environment data created by simulator
    def get_data(self):
        return simulator.get_data("temperature", self.env)

class HumiditySensor:
    # ideal humidity between 65-75% during night, 80% during day
    def __init__(self, environment):
        self.env = environment
    # get environment data created by simulator
    def get_data(self):
        return simulator.get_data("humidity", self.env)

class LightSensor:
    # ideal light spectrum between 600 - 700nm
    def __init__(self, environment):
        self.env = environment
    # get environment data created by simulator
    def get_data(self):
        return simulator.get_data("light", self.env)

def initialize_sensors(environment):
    temperature_sensor = TemperatureSensor(environment)
    humidity_sensor = HumiditySensor(environment)
    light_sensor = LightSensor(environment)
    
    # put sensors into the output dictionary
    sensors = {"temperature": temperature_sensor, "humidity": humidity_sensor, "light": light_sensor}

    return sensors