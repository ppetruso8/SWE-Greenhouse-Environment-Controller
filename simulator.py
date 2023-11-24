'''
Simulator generating sensor readings of environment variables.
'''

import random
    
# get range for possible sensors data changes to better depict real world scenario
changes = {
    "temperature": 0.3,
    "humidity": 2,
    "light": 10
}

# generate data for sensors
def get_data(sensor: str, environment):
    '''
    sensor -- type of sensor for which the data should be generated
    environment -- instance of Environment class
    '''
    if sensor not in changes:
        raise ValueError("Sensor type %s is not valid.", sensor)

    # calculate change for appropriate sensor
    if sensor == "temperature":
        change = random.uniform(-changes[sensor], changes[sensor])                
    else:
        change = random.randint(-changes[sensor], changes[sensor])

    updated_value = environment.get_environment(sensor) + change

    # apply boundaries to the environmental variable values and apply changes
    if sensor == "temperature":
        if updated_value > 40:
            environment.set_environment(sensor, 40.0)
        elif updated_value < 15:
            environment.set_environment(sensor, 15.0)
    elif sensor == "humidity":
        if updated_value > 100:
                environment.set_environment(sensor, 100)
        elif updated_value < 40:
                environment.set_environment(sensor, 40)
    elif sensor == "light":
        if updated_value > 850:
            environment.set_environment(sensor, 850)
        elif updated_value < 100:
            environment.set_environment(sensor, 100)

    environment.set_environment(sensor, updated_value)        

    # return generated data
    if sensor == "temperature":
        return round(updated_value, 2)
    else:
        return updated_value