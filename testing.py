'''testing and validation'''
import unittest
from controller import Environment
from simulator import get_simulator_data
from sensors import TemperatureSensor, HumiditySensor, LightSensor
from actuators import Heater, Humidifier, Lights

class TestEnvironment(unittest.TestCase):
    def test_initialization(self):
        ''' 
        Test that the environment is initialized with passed in values
        '''
        env = Environment(25.0, 60, 550)
        self.assertEqual(env.get_environment(), {'temperature': 25.0, 'humidity': 60, 'light': 550}, "environment not initialized correctly")
        self.assertEqual(env.get_environment_variable("temperature"), 25.0, "temperature not initialized correctly")
        self.assertEqual(env.get_environment_variable("humidity"), 60, "humidity not initialized correctly")
        self.assertEqual(env.get_environment_variable("light"), 550, "lights not initialized correctly")

    def test_setting_environment(self):
        ''' 
        Test that it is possible to change the environment factor's value 
        '''
        env = Environment(25.0, 60, 550)
        env.set_environment("temperature", 20.5)
        self.assertEqual(env.get_environment_variable("temperature"), 20.5, "temperature change failure")
        env.set_environment("humidity", 70)
        self.assertEqual(env.get_environment_variable("humidity"), 70, "humidity change failure")
        env.set_environment("light", 600)
        self.assertEqual(env.get_environment_variable("light"), 600, "light spectrum change failure")

    def test_setting_environment_invalid_input(self):
        '''
        Test that the appropriate exception is raised when invalid input is passed in while changing environment factor's value
        '''
        env = Environment(25.0, 60, 550)

        with self.assertRaises(TypeError):
            env.set_environment(1, "x")

        with self.assertRaises(ValueError):
            env.set_environment("x", 1)

    def test_getting_variable_invalid_input(self):
        '''
        Test if exception is raised when invalid input is passed in while getting the value of environment factor
        '''
        env = Environment(25.0, 60, 550)

        with self.assertRaises(ValueError):
            env.get_environment_variable("x")

class TestSimulator(unittest.TestCase):
    def test_simulate_data(self):
        '''
        Test that the simulated data is within boundaries
        '''
        env = Environment(25.0, 60, 550)
        simulated_temp = get_simulator_data("temperature", env)
        self.assertGreaterEqual(simulated_temp, 15.0, "simulated temperature is less than 15.0")
        self.assertLessEqual(simulated_temp, 40.0, "simulated temperature is higher than 40.0")
        simulated_humidity = get_simulator_data("humidity", env)
        self.assertIn(simulated_humidity, range(40, 101), "simulated humidity is not within boundaries")
        simulated_light = get_simulator_data("light", env)
        self.assertIn(simulated_light, range(0, 851), "simulated light spectrum level is not within boundaries")

class TestSensors(unittest.TestCase):
    def test_temperature_sensor(self):
        '''
        Test that temperature sensor is able to fetch data
        '''
        env = Environment(25.0, 60, 550)
        temp_sensor = TemperatureSensor(env)
        simulator_data = temp_sensor.get_simulator_data()
        self.assertTrue(15.0 <= simulator_data <= 40.0, "error fetching temperature data from simulator")
        env_data = temp_sensor.get_environment_data(env)
        self.assertTrue(15.0 <= env_data <= 40.0, "error fetching temperature data from environment")

    def test_humidity_sensor(self):
        '''
        Test that humidity sensor is able to fetch data
        '''
        env = Environment(25.0, 60, 550)
        humidity_sensor = HumiditySensor(env)
        simulator_data = humidity_sensor.get_simulator_data()
        self.assertTrue(40 <= simulator_data <= 100, "error fetching humidity data from simulator")
        env_data = humidity_sensor.get_environment_data(env)
        self.assertTrue(40 <= env_data <= 100, "error fetching humidity data from environment")

    def test_light_sensor(self):
        '''
        Test that light spectrum sensor is able to fetch data
        '''
        env = Environment(25.0, 60, 550)
        light_sensor = LightSensor(env)
        simulator_data = light_sensor.get_simulator_data()
        self.assertTrue(0 <= simulator_data <= 850, "error fetching light spectrum data from simulator")
        env_data = light_sensor.get_environment_data(env)
        self.assertTrue(0 <= env_data <= 850, "error fetching light sensor data from environment")

class TestActuators(unittest.TestCase):
    #NOTE: add test to see what happens when user inputs value out of boundaries
    def test_heater(self):
        '''
        Test that heater updates the environment
        '''
        env = Environment(25.0, 60, 550)
        heater = Heater(env)
        
        heater.change_temp(30.0)
        self.assertEqual(env.get_environment_variable("temperature"), 30.0, "heater not updating environment")

    def test_humidifier(self):
        '''
        Test that humidifier updates the environment
        '''
        env = Environment(25.0, 60, 550)
        humidifier = Humidifier(env)
        
        humidifier.change_humidity(80)
        self.assertEqual(env.get_environment_variable("humidity"), 80, "humidifier not updating environment")

    def test_lights(self):
        '''
        Test that lights update the environment
        '''
        env = Environment(25.0, 60, 550)
        lights = Lights(env)
        
        lights.change_light(700)
        self.assertEqual(env.get_environment_variable("light"), 700, "lights not updating environment")

    def test_heater_invalid_input(self):
        '''
        Test if appropriate exception is raised when invalid parameter is passed in to change_temp
        '''
        env = Environment(25.0, 60, 550)
        heater = Heater(env)

        with self.assertRaises(TypeError):
            heater.change_temp("x")

    def test_humidifier_invalid_input(self):
        '''
        Test if appropriate exception is raised when invalid parameter is passed in to change_humidity
        '''
        env = Environment(25.0, 60, 550)
        humidifier = Humidifier(env)

        with self.assertRaises(TypeError):
            humidifier.change_humidity("x")

    def test_lights_invalid_input(self):
        '''
        Test if appropriate exception is raised when invalid parameter is passed in to change_light
        '''
        env = Environment(25.0, 60, 550)
        lights = Lights(env)

        with self.assertRaises(TypeError):
            lights.change_light("x")

if __name__ == '__main__':
    unittest.main()