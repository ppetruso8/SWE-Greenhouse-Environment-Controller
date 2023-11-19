'''
Simulator generating sensor readings of environment.
'''

import random

# initial ideal environment state
environment = {
    "temperature": 25.0,
    "humidity": 80,
    "light": 550
}

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

    for variable in changes:
        # get the change of the value for each environment variable
        if variable == "temperature":
            change = random.uniform(-changes[variable], changes[variable])                
        else:
            change = random.randint(-changes[variable], changes[variable])

        updated_value = environment[variable] + change

        # apply boundaries to the environmental variable values and apply changes
        if variable == "temperature":
            if updated_value > 40:
                environment[variable] = 40
            elif updated_value < 15:
                environment[variable] = 15
            else:
                environment[variable] = updated_value
        elif variable == "humidity":
            if updated_value > 100:
                    environment[variable] = 100
            elif updated_value < 40:
                    environment[variable] = 40
            else:
                environment[variable] = updated_value
        elif variable == "light":
            if updated_value > 850:
                environment[variable] = 850
            elif updated_value < 100:
                environment[variable] = 100
            else:
                environment[variable] = updated_value        

    # return generated data
    if sensor == "temperature":
        return round(environment["temperature"], 2)
    elif sensor == "humidity":
        return environment["humidity"]
    elif sensor == "light":
        return environment["light"]
    else:
        raise ValueError("Sensor type %s is not valid.", sensor)