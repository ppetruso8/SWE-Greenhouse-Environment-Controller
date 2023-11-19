'''
Module containing sensors classes.
Sensors get data from simulator, process them and send data to the controller.
'''

import simluator

class TemperatureSensor:
    # get environment data created by simulator
    def get_data(self):
        return simluator.get_data("temperature")

class HumiditySensor:
    # get environment data created by simulator
    def get_data(self):
        return simluator.get_data("humidity")

class LightSensor:
    # get environment data created by simulator
    def get_data(self):
        return simluator.get_data("light")

def initialize_sensors():
    temperature_sensor = TemperatureSensor
    humidity_sensor = HumiditySensor
    light_sensor = LightSensor
    
    # put sensors into the output dictionary
    sensors = {"temperature": temperature_sensor, "humidity": humidity_sensor, "light": light_sensor}

    return sensors