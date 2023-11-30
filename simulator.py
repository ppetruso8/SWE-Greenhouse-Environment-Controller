'''
Simulator generating sensor readings of environment variables.

Simulator simulates realistic changes in the greenhouse environment.
'''

import random
    
# define range for possible changes for each sensor to simulate real world scenario
changes = {
    "temperature": 0.3,
    "humidity": 2,
    "light": 10
}

# generate data for sensors
def get_simulator_data(sensor: str, environment):
    ''' Generate data for a specific sensor in environment based on current environment state.

    sensor -- type of sensor for which the data should be generated
    environment -- instance of Environment class
    '''
    if type(sensor) != str:
        raise TypeError("Sensor type must be passed in as a string.")
    
    if sensor not in changes:
        raise ValueError("Sensor type %s is not valid." % sensor)

    
    # calculate a random change for appropriate sensor and calculate updated value
    if sensor == "temperature":
        change = random.uniform(-changes[sensor], changes[sensor])
        updated_value = round(environment.get_environment_variable(sensor) + change, 2)
    else:
        change = random.randint(-changes[sensor], changes[sensor])
        updated_value = environment.get_environment_variable(sensor) + change    

    # apply boundaries to the environmental variable values
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
        elif updated_value < 0:
            environment.set_environment(sensor, 0)

    environment.set_environment(sensor, updated_value)     

    # return generated data
    return updated_value