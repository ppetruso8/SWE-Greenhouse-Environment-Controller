'''testing and validation'''
import unittest
from unittest import mock
from controller import Environment, initialize_actuators, initialize_sensors, work
from simulator import get_simulator_data
from sensors import TemperatureSensor, HumiditySensor, LightSensor
from actuators import Heater, Humidifier, Lights

class TestSettingEnvironment(unittest.TestCase):
    '''
    Class containing tests for the set_environment method
    '''
    def setUp(self) -> None:
        self.env = Environment(25.0, 60, 550)
    
    def test_setting_environment_temperature(self):
        '''
        Test if temperature value is changed correctly after passing valid input value
        '''
        self.env.set_environment("temperature", 22.0)
        self.assertEqual(self.env.get_environment_variable("temperature"), 22.0, "error setting temperature value")
    
    def test_setting_environment_humidity(self):
        '''
        Test if humidity value is changed correctly after passing valid input value
        '''
        self.env.set_environment("humidity", 70)
        self.assertEqual(self.env.get_environment_variable("humidity"), 70, "error setting humidity value")

    def test_setting_environment_light(self):
        '''
        Test if light spectrum value is changed correctly after passing valid input value
        '''
        self.env.set_environment("light", 650)
        self.assertEqual(self.env.get_environment_variable("light"), 650, "error setting light spectrum value")

    def test_setting_environment_invalid_input_variable_value(self):
        '''
        Test if exception is raised when invalid variable is passed in while changing environment factor's value
        '''
        with self.assertRaises(ValueError):
            self.env.set_environment("moisture", 25)

    def test_setting_environment_high_temperature(self):
        '''
        Test if exception is raised when too high temperature value is passed in while changing environment factor's value
        '''
        with self.assertRaises(ValueError):
            self.env.set_environment("temperature", 50.0)

    def test_setting_environment_low_temperature(self):
        '''
        Test if exception is raised when too low temperature value is passed in while changing environment factor's value
        '''
        with self.assertRaises(ValueError):
            self.env.set_environment("temperature", 10.0)

    def test_setting_environment_high_humidity(self):
        '''
        Test if exception is raised when too high humidity value is passed in while changing environment factor's value
        '''
        with self.assertRaises(ValueError):
            self.env.set_environment("humidity", 150)

    def test_setting_environment_low_humidity(self):
        '''
        Test if exception is raised when too low humidity value is passed in while changing environment factor's value
        '''
        with self.assertRaises(ValueError):
            self.env.set_environment("humidity", 0)

    def test_setting_environment_high_light(self):
        '''
        Test if exception is raised when too high light spectrum value is passed in while changing environment factor's value
        '''
        with self.assertRaises(ValueError):
            self.env.set_environment("light", 1000)

    def test_setting_environment_low_light(self):
        '''
        Test if exception is raised when too low light spectrum value is passed in while changing environment factor's value
        '''
        with self.assertRaises(ValueError):
            self. env.set_environment("light", 0)
    
    def test_setting_environment_temperature_upper_boundary(self):
        '''
        Test if the temperature is set when upper boundary value is passed in
        '''
        self.env.set_environment("temperature", 40.0)
        self.assertEqual(self.env.get_environment_variable("temperature"), 40.0, 
                         "environment temperature not set when upper boundary value passed in")
        
    def test_setting_environment_humidity_upper_boundary(self):
        '''
        Test if the humidity is set when upper boundary value is passed in
        '''
        self.env.set_environment("humidity", 100)
        self.assertEqual(self.env.get_environment_variable("humidity"), 100, 
                         "environment humidity not set when upper boundary value passed in")
        
    def test_setting_environment_light_upper_boundary(self):
        '''
        Test if the light spectrum value is set when upper boundary value is passed in
        '''
        self.env.set_environment("light", 850)
        self.assertEqual(self.env.get_environment_variable("light"), 850, 
                         "environment light spectrum value not set when upper boundary value passed in")
        
    def test_setting_environment_temperature_lower_boundary(self):
        '''
        Test if the temperature is set when lower boundary value is passed in
        '''
        self.env.set_environment("temperature", 15.0)
        self.assertEqual(self.env.get_environment_variable("temperature"), 15.0, 
                         "environment temperature not set when lower boundary value passed in")
        
    def test_setting_environment_humidity_lower_boundary(self):
        '''
        Test if the humidity is set when lower boundary value is passed in
        '''
        self.env.set_environment("humidity", 40)
        self.assertEqual(self.env.get_environment_variable("humidity"), 40, 
                         "environment humidity not set when lower boundary value passed in")
        
    def test_setting_environment_light_lower_boundary(self):
        '''
        Test if the light is set when lower boundary value is passed in
        '''
        self.env.set_environment("light", 150)
        self.assertEqual(self.env.get_environment_variable("light"), 150, 
                         "environment light spectrum value not set when lower boundary value passed in")


class TestGettingEnvironment(unittest.TestCase):
    '''
    Class containing tests for the set_environment method
    '''
    def setUp(self) -> None:
        self.env = Environment(25.0, 60, 550)   

    def test_getting_temperature_variable(self):
        '''
        Test if it is possible to fetch a value of temperature from environment
        '''
        self.assertEqual(self.env.get_environment_variable("temperature"), 25.0, 
                         "temperature was not fetched from environment")
        
    def test_getting_humidity_variable(self):
        '''
        Test if it is possible to fetch a value of humidity from environment
        '''
        self.assertEqual(self.env.get_environment_variable("humidity"), 60, 
                         "humidity was not fetched from environment")
        
    def test_getting_light_variable(self):
        '''
        Test if it is possible to fetch a value of light spectrum from environment
        '''
        self.assertEqual(self.env.get_environment_variable("light"), 550, 
                         "light was not fetched from environment")

    def test_getting_variable_invalid_input(self):
        '''
        Test if exception is raised when invalid input is passed in while getting the value of environment factor
        '''
        with self.assertRaises(ValueError):
            self.env.get_environment_variable("x")

# class TestSensors(unittest.TestCase):
    # def test_temperature_sensor(self):
    #     '''
    #     Test that temperature sensor is able to fetch data
    #     '''
    #     env = Environment(25.0, 60, 550)
    #     temp_sensor = TemperatureSensor(env)

    #     simulator_data = temp_sensor.get_simulator_data()
    #     self.assertEqual(simulator_data, env.get_environment_variable("temperature"), 
    #                      "error fetching temperature data from simulator")

    #     env_data = temp_sensor.get_environment_data(env)
    #     self.assertEqual(env_data, env.get_environment_variable("temperature"), 
    #                      "error fetching temperature data from environment")

    # def test_humidity_sensor(self):
    #     '''
    #     Test that humidity sensor is able to fetch data
    #     '''
    #     env = Environment(25.0, 60, 550)
    #     humidity_sensor = HumiditySensor(env)

    #     simulator_data = humidity_sensor.get_simulator_data()
    #     self.assertEqual(simulator_data, env.get_environment_variable("humidity"), 
    #                      "error fetching humidity data from simulator")

    #     env_data = humidity_sensor.get_environment_data(env)
    #     self.assertEqual(env_data, env.get_environment_variable("humidity"), 
    #                      "error fetching humidity data from environment")       

    # def test_light_sensor(self):
    #     '''
    #     Test that light spectrum sensor is able to fetch data
    #     '''
    #     env = Environment(25.0, 60, 550)
    #     light_sensor = LightSensor(env)

    #     simulator_data = light_sensor.get_simulator_data()
    #     self.assertEqual(simulator_data, env.get_environment_variable("light"), 
    #                      "error fetching light spectrum data from simulator")

    #     env_data = light_sensor.get_environment_data(env)
    #     self.assertEqual(env_data, env.get_environment_variable("light"), 
    #                      "error fetching light spectrum data from environment")  
        
class TestHeaterChangeTemp(unittest.TestCase):
    def setUp(self) -> None:
        self.env = Environment(25.0, 60, 550)
        self.heater = Heater(self.env) 

    def test_p1(self):
        with self.assertRaises(TypeError):
            self.heater.change_temp("x")

    def test_p2(self):
        self.env.set_environment("temperature", 40.0)
        self.heater.change_temp(50)
        self.assertEqual(self.env.get_environment_variable("temperature"), 40.0)

    def test_p3(self):
        self.env.set_environment("temperature", 25.2)

        with mock.patch('random.uniform', return_value=24.95):
            self.heater.change_temp(25.0)
            self.assertEqual(self.env.get_environment_variable("temperature"), 25.0)

    def test_p4(self):
       self.env.set_environment("temperature", 15.3)

       with mock.patch('random.uniform', return_value=15.0):
           self.heater.change_temp(10.0) 
           self.assertEqual(self.env.get_environment_variable("temperature"), 15.0)

    def test_p5(self):
        self.env.set_environment("temperature", 25.0)
        
        with mock.patch('random.uniform', return_value=25.3):
           self.heater.change_temp(25.2)
           self.assertEqual(self.env.get_environment_variable("temperature"), 25.2)

    def test_p6(self):
        self.env.set_environment("temperature", 25.0)
        
        with mock.patch('random.uniform', return_value=25.3):
           self.heater.change_temp(25.3)
           self.assertEqual(self.env.get_environment_variable("temperature"), 25.3)

# class TestWorkLoop(unittest.TestCase):
#     def test_test_statement(self):
#         pass
    
#     def test_break(self):
#         pass

# class TestActuatorActivation(unittest.TestCase):        
#     def test_actuators_activation(self):
#         '''
#         Test if actuators activate when the environment is not in ideal condition
#         '''
#         # higher value
#         env = Environment(30.0, 90, 800)
#         sensors = initialize_sensors(env)
#         actuators = initialize_actuators(env)

#         work(env, sensors, actuators, 1)
#         self.assertEqual(env.get_environment_variable("temperature"), 27.0, 
#                          "heater not activated when environment not ideal")
#         self.assertEqual(env.get_environment_variable("humidity"), 80, 
#                          "humidifier not activated when environment not ideal")
#         self.assertEqual(env.get_environment_variable("light"), 700, 
#                          "lights not activated when environment not ideal")
        
#         # lower value
#         env2 = Environment(17.0, 45, 300)
#         sensors = initialize_sensors(env2)
#         actuators = initialize_actuators(env2)

#         work(env2, sensors, actuators, 1)
#         self.assertEqual(env2.get_environment_variable("temperature"), 21.0, 
#                          "heater not activated when environment not ideal")
#         self.assertEqual(env2.get_environment_variable("humidity"), 65, 
#                          "humidifier not activated when environment not ideal")
#         self.assertEqual(env2.get_environment_variable("light"), 600, 
#                          "lights not activated when environment not ideal")

if __name__ == '__main__':
    unittest.main()