'''testing and validation'''
import unittest
from controller import Environment, initialize_actuators, initialize_sensors, work
from simulator import get_simulator_data
from sensors import TemperatureSensor, HumiditySensor, LightSensor
from actuators import Heater, Humidifier, Lights

class TestEnvironment(unittest.TestCase):
    def test_setting_environment_valid_input(self):
        '''
        Test if environment value is changed correctly after passing valid input value
        '''
        env = Environment(25.0, 60, 550)

        env.set_environment("temperature", 22.0)
        self.assertEqual(env.get_environment_variable("temperature"), 22.0, "error setting temperature value")

        env.set_environment("humidity", 70)
        self.assertEqual(env.get_environment_variable("humidity"), 70, "error setting humidity value")

        env.set_environment("light", 650)
        self.assertEqual(env.get_environment_variable("light"), 650, "error setting light spectrum value")

    def test_setting_environment_invalid_input(self):
        '''
        Test if exception is raised when invalid input is passed in while changing environment factor's value
        '''
        env = Environment(25.0, 60, 550)

        with self.assertRaises(TypeError):
            env.set_environment(1, 25)

        with self.assertRaises(ValueError):
            env.set_environment("moisture", 25)

        with self.assertRaises(ValueError):
            env.set_environment("temperature", 50.0)
            env.set_environment("temperature", 10.0)

            env.set_environment("humidity", 150)
            env.set_environment("humidity", 0)

            env.set_environment("light", 1000)
            env.set_environment("light", 0)
    
    def test_setting_environment_boundaries(self):
        '''
        Test if the environment is set when a boundary value is passed in
        '''
        env = Environment(25.0, 60, 550)

        # upper boundary
        env.set_environment("temperature", 40.0)
        self.assertEqual(env.get_environment_variable("temperature"), 40.0, 
                         "environment temperature not set when upper boundary value passed in")
        env.set_environment("humidity", 100)
        self.assertEqual(env.get_environment_variable("humidity"), 100, 
                         "environment humidity not set when upper boundary value passed in")
        env.set_environment("light", 850)
        self.assertEqual(env.get_environment_variable("light"), 850, 
                         "environment light spectrum value not set when upper boundary value passed in")
        
        # lower boundary
        env.set_environment("temperature", 15.0)
        self.assertEqual(env.get_environment_variable("temperature"), 15.0, 
                         "environment temperature not set when lower boundary value passed in")
        env.set_environment("humidity", 40)
        self.assertEqual(env.get_environment_variable("humidity"), 40, 
                         "environment humidity not set when lower boundary value passed in")
        env.set_environment("light", 150)
        self.assertEqual(env.get_environment_variable("light"), 150, 
                         "environment light spectrum value not set when lower boundary value passed in")
        
    def test_getting_variable_invalid_input(self):
        '''
        Test if exception is raised when invalid input is passed in while getting the value of environment factor
        '''
        env = Environment(25.0, 60, 550)

        with self.assertRaises(ValueError):
            env.get_environment_variable("x")

        with self.assertRaises(TypeError):
            env.get_environment_variable(2)

    def test_get_ideal_conditions(self):
        '''
        Test if get_user_setting method returns the dictionary containing user settings
        '''
        env = Environment(25.0, 60, 550)
        self.assertEqual(env.get_ideal_conditions(),
                         {'temp_upper': 27.0, 'temp_lower': 21.0, 'humidity_upper': 80, 'humidity_lower': 65, 'light_upper': 700, 'light_lower': 600}, 
                         "ideal condition dictionary not received correctly")

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

class TestActuators(unittest.TestCase):
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

class TestActuatorActivation(unittest.TestCase):        
    def test_actuators_activation(self):
        '''
        Test if actuators activate when the environment is not in ideal condition
        '''
        # higher value
        env = Environment(30.0, 90, 900)
        sensors = initialize_sensors(env)
        actuators = initialize_actuators(env)

        work(env, sensors, actuators, 1)
        self.assertEqual(env.get_environment_variable("temperature"), 27.0, 
                         "heater not activated when environment not ideal")
        self.assertEqual(env.get_environment_variable("humidity"), 80, 
                         "humidifier not activated when environment not ideal")
        self.assertEqual(env.get_environment_variable("light"), 700, 
                         "lights not activated when environment not ideal")
        
        # lower value
        env2 = Environment(17.0, 20, 300)
        sensors = initialize_sensors(env2)
        actuators = initialize_actuators(env2)

        work(env2, sensors, actuators, 1)
        self.assertEqual(env2.get_environment_variable("temperature"), 21.0, 
                         "heater not activated when environment not ideal")
        self.assertEqual(env2.get_environment_variable("humidity"), 65, 
                         "humidifier not activated when environment not ideal")
        self.assertEqual(env2.get_environment_variable("light"), 600, 
                         "lights not activated when environment not ideal")

if __name__ == '__main__':
    unittest.main()