'''
Module containing sensors classes.
Sensors get data from simulator, process them and send data to the controller.
'''

import simulator

class TemperatureSensor:
    # ideal temperature between 21 to 27°C
    # get environment data created by simulator
    def get_data(self):
        return simulator.get_data("temperature")

class HumiditySensor:
    # ideal humidity between 65-75% during night, 80% during day
    # get environment data created by simulator
    def get_data(self):
        return simulator.get_data("humidity")

class LightSensor:
    # ideal green light spectrum between 500 - 600nm
    # get environment data created by simulator
    def get_data(self):
        return simulator.get_data("light")

def initialize_sensors():
    temperature_sensor = TemperatureSensor()
    humidity_sensor = HumiditySensor()
    light_sensor = LightSensor()
    
    # put sensors into the output dictionary
    sensors = {"temperature": temperature_sensor, "humidity": humidity_sensor, "light": light_sensor}

    return sensors