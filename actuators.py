'''
Manage actuators responsible for making changes to the greenhouse environment values.

Controller can use appropriate actuator class to adjust the greenhouse environment conditions
    Heaters for temperature
    Humidifier for humidity
    Lights for light spectrum

Environment variables boundaries:
    - temperature: 15.0-40.0
    - humidity: 40-100
    - light: 100-850

NOTE: if that is too difficult, we do not need user input (it could be better but it's up to us), 
but we can only simulate values, and raise some warnings when the environment condition is not 
optimal and based on that make changes - it's up to you!
'''
import random

class Heater:
    ''' Actuator class for controlling temperature of environment

    Attributes:
    env -- environment instance representing current environment
    max -- maximum allowed temperature
    min -- minimum allowed temperature
    change -- maximum change in temperature in one step
    '''
    def __init__(self, environment):
        ''' Initialize heater and set boundaries
        
        environment -- environment instance
        '''
        self.env = environment
        self.max = 40
        self.min = 15
        self.change = 0.3

    def change_temp(self, target_temperature: float):
        ''' Gradually change temperature values towards the target temperature

        target_temperature -- desired temperature to reach
        '''
        if type(target_temperature) == int:
            target_temperature = float(target_temperature)

        if type(target_temperature) != float:
            raise TypeError("Target temperature must be passed in as a float.")

        current_temp = self.env.get_environment("temperature")

        # temperature boundaries
        if target_temperature > self.max:
            target_temperature = self.max
        elif target_temperature < self.min:
            target_temperature = self.min

        # gradually change the temperature
        while current_temp != target_temperature:
            if current_temp > target_temperature:
                new_temp = random.uniform(current_temp, current_temp+self.change)

                if new_temp > target_temperature:
                    current_temp = target_temperature
                else:
                    current_temp = new_temp
            elif current_temp < target_temperature:
                new_temp = random.uniform(current_temp-self.change, current_temp)

                if new_temp < target_temperature:
                    current_temp = target_temperature
                else:
                    current_temp = new_temp
            
            try:
                self.env.set_environment("temperature", current_temp)
            except Exception as e:
                print("Heater: error encountered while updating environment: %s", e)

class Humidifier:
    ''' Actuator class for controlling humidity of environment

    Attributes:
    env -- environment instance representing current environment
    max -- maximum allowed humidity
    min -- minimum allowed humidity
    change -- maximum change in humidity in one step
    '''
    def __init__(self, environment):
        ''' Initialize humidifier and set boundaries
        
        environment -- environment instance
        '''
        self.env = environment
        self.max = 100
        self.min = 40
        self.change = 2

    def change_humidity(self, target_humidity: int):
        ''' Gradually change humidity values towards the target humidity

        target_humidity -- desired humidity to reach
        '''
        if type(target_humidity) != int:
            raise TypeError("Target humidity must be passed in as an integer.")
        
        current_humidity = self.env.get_environment("humidity")

        # humidity boundaries
        if target_humidity > self.max:
            target_humidity = self.max
        elif target_humidity < self.min:
            target_humidity = self.min

        # gradually change the humidity
        while current_humidity != target_humidity:
            if current_humidity > target_humidity:
                new_humidity = random.uniform(current_humidity, current_humidity+self.change)

                if new_humidity > target_humidity:
                    current_humidity = target_humidity
                else:
                    current_humidity = new_humidity
            elif current_humidity < target_humidity:
                new_humidity = random.uniform(current_humidity-self.change, current_humidity)

                if new_humidity < target_humidity:
                    current_humidity = target_humidity
                else:
                    current_humidity = new_humidity
            
            try:
                self.env.set_environment("humidity", current_humidity)
            except Exception as e:
                print("Humidifier: error encountered while updating environment: %s", e)

class Lights:
    ''' Actuator class for controlling light spectrum of environment

    Attributes:
    env -- environment instance representing current environment
    max -- maximum allowed light spectrum value
    min -- minimum allowed light spectrum value
    change -- maximum change in light spectrum value in one step
    '''
    def __init__(self, environment):
        ''' Initialize lights and set boundaries
        
        environment -- environment instance
        '''
        self.env = environment
        self.max = 850
        self.min = 100
        self.change = 10

    def change_light(self, target_light: int):
        ''' Gradually change light spectrum towards the target light spectrum value

        target_light -- desired light spectrum value to reach
        '''
        if type(target_light) != int:
            raise TypeError("Target light spectrum value must be passed in as an integer.")
        
        current_light = self.env.get_environment("light")

        # light spectrum boundaries
        if target_light > self.max:
            target_light = self.max
        elif target_light < self.min:
            target_light = self.min

        # gradually change the light
        while current_light != target_light:
            if current_light > target_light:
                new_light = random.uniform(current_light, current_light+self.change)

                if new_light > target_light:
                    current_light = target_light
                else:
                    current_light = new_light
            elif current_light < target_light:
                new_light = random.uniform(current_light-self.change, current_light)

                if new_light < target_light:
                    current_light = target_light
                else:
                    current_light = new_light
            
            try:
                self.env.set_environment("light", current_light)
            except Exception as e:
                print("Lights: error encountered while updating environment: %s", e)

def initialize_actuators(environment):
    heater = Heater(environment)
    humidifier = Humidifier(environment)
    lights = Lights(environment)
    
    # put actuators into the output dictionary
    actuators = {"heater": heater, "humidifier": humidifier, "lights": lights}

    return actuators