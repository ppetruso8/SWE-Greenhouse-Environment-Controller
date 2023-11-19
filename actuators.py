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

from simulator import get_environment, set_environment