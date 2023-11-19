'''
Simulator generating sensor readings of environment.
'''

import random

def get_data(sensor):
    '''
    sensor -- type of sensor for which the data should be generated
    '''
    # create data for temperature, multiply by 10 for ability to later "convert" to float (°C)
    min_temp = 15*10
    max_temp = 33*10
    temperature = round((random.randint(min_temp,max_temp) / 10.0), 2)

    # create data for humidity (%) 
    humidity = random.randint(60,90)

    # create data for green light
    light = random.randint(450,650)

    # return generated data
    if sensor == "temperature":
        return temperature
    elif sensor == "humidity":
        return humidity
    elif sensor == "light":
        return light
    else:
        raise ValueError("Sensor type %s is not valid.", sensor)