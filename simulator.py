'''
Simulator simulating greenhouse environment and generating sensor readings of environment variables.
'''

import random

# initial environment state
environment = {
    "temperature": 25.0,
    "humidity": 80,
    "light": 550
}

# change environment state
def set_environment(variable, value):
    if variable in environment:
        environment[variable] = value
    else:
        raise ValueError("Invalid environment variable %s", variable)
    
# get current environment state
def get_environment():
    return environment
    
# generate data for sensors
def get_data(sensor):
    '''
    sensor -- type of sensor for which the data should be generated
    '''
    # get range for possible sensors data changes to better depict real world scenario
    changes = {
        "temperature": 0.3,
        "humidity": 2,
        "light": 10
    }

    # calculate change for appropriate sensor
    if sensor == "temperature":
        change = random.uniform(-changes[sensor], changes[sensor])                
    else:
        change = random.randint(-changes[sensor], changes[sensor])


    updated_value = environment[sensor] + change

    # apply boundaries to the environmental variable values and apply changes
    if sensor == "temperature":
        if updated_value > 40:
            environment[sensor] = 40
        elif updated_value < 15:
            environment[sensor] = 15
        else:
            environment[sensor] = updated_value
    elif sensor == "humidity":
        if updated_value > 100:
                environment[sensor] = 100
        elif updated_value < 40:
                environment[sensor] = 40
        else:
            environment[sensor] = updated_value
    elif sensor == "light":
        if updated_value > 850:
            environment[sensor] = 850
        elif updated_value < 100:
            environment[sensor] = 100
        else:
            environment[sensor] = updated_value        

    # return generated data
    if sensor == "temperature":
        return round(environment["temperature"], 2)
    elif sensor == "humidity":
        return environment["humidity"]
    elif sensor == "light":
        return environment["light"]
    else:
        raise ValueError("Sensor type %s is not valid.", sensor)