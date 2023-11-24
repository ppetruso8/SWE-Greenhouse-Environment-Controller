'''
Manage devices responsible for making changes to the greenhouse environment values.
When user sets needed parameters, pass here the values to appropriate class
    Heaters for temperature
    Humidifier for humidity
    Lights for light spectrum
and change values in environment gradually

Get environment by calling get_environment from simulator
Change environment by calling set_environment(variable, value), where
    variable: ["temperature", "humidity", "light"]
    value is within boundaries:
        - temperature: 15-40
        - humidity: 40-100
        - light: 100-850
--> make sure to check whether the values from user are correct and within ranges

NOTE: if that is too difficult, we do not need user input (it could be better but it's up to us), 
but we can only simulate values, and raise some warnings when the environment condition is not 
optimal and based on that make changes - it's up to you!
'''
import random

class Heater:
    def __init__(self, environment):
        self.env = environment
        self.max = 40
        self.min = 15

        # possible temperature change in one step
        self.change = 0.3

    def change_temp(self, target_temperature: float):
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
            
            self.env.set_environment("temperature", current_temp)

class Humidifier:
    def __init__(self, environment):
        self.env = environment
        self.max = 100
        self.min = 40

        # possible humidity change in one step
        self.change = 2

    def change_humidity(self, target_humidity: int):
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
            
            self.env.set_environment("humidity", current_humidity)

class Lights:
    def __init__(self, environment):
        self.env = environment
        self.max = 850
        self.min = 100

        # possible light spectrum change in one step
        self.change = 10

    def change_light(self, target_light: int):
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
            
            self.env.set_environment("light", current_light)

def initialize_actuators(environment):
    heater = Heater(environment)
    humidifier = Humidifier(environment)
    lights = Lights(environment)
    
    # put actuators into the output dictionary
    actuators = {"heater": heater, "humidifier": humidifier, "lights": lights}

    return actuators