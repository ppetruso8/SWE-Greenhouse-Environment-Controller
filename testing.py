'''testing and validation'''
import unittest
from controller import Environment, initialize_actuators, initialize_sensors, work
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

    def test_initialization_invalid_input(self):
        '''
        Test if environment handles invalid parameter being passed while initializing
        '''
        with self.assertRaises(TypeError):
            env1 = Environment("x", 60, 550)
            env2 = Environment(25.0, "x", 550)
            env3 = Environment(25.0, 60, "x")

        # test if temperature is converted to float if it is passed in as integer
        env = Environment(25, 60, 550)
        self.assertEqual(env.get_environment(), {'temperature': 25.0, 'humidity': 60, 'light': 550}, 
                         "integer temperature value not converted to float during environment initialization")

    def test_setting_environment_invalid_input(self):
        '''
        Test if exception is raised when invalid input is passed in while changing environment factor's value
        '''
        env = Environment(25.0, 60, 550)

        with self.assertRaises(TypeError):
            env.set_environment(1, 25)

        with self.assertRaises(ValueError):
            env.set_environment("x", 25)

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

    def test_get_user_setting(self):
        '''
        Test if get_user_setting method returns the dictionary containing user settings
        '''
        env = Environment(25.0, 60, 550)
        self.assertEqual(env.get_user_setting(), {'user_temp': None, 'user_humidity': None, 'user_light': None}, "user setting dictionary not received correctly")

    def test_set_user_setting(self):
        '''
        Test if user_setting dictionary is updated successfully
        '''
        env = Environment(25.0, 60, 550)

        env.set_user_settings(30.0, 50, 600)
        self.assertEqual(env.get_user_setting(), {'user_temp': 30.0, 'user_humidity': 50, 'user_light': 600})

    def test_set_user_settings_invalid_input(self):
        '''
        Test if environment handles invalid parameter being passed while changing user_setting
        '''
        env = Environment(25.0, 60, 550)

        with self.assertRaises(TypeError):
            env.set_user_settings(temperature = "x")
            env.set_user_settings(humidity = "x")
            env.set_user_settings(light = "x")

        # test if temperature is converted to float if it is passed in as integer 
        env.set_user_settings(temperature = 20)
        self.assertEqual(env.get_user_setting(), {'user_temp': 20.0, 'user_humidity': None, 'user_light': None}, 
                         "integer temperature value not converted to float when updating user_settings")
        

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
        self.assertEqual(simulator_data, env.get_environment_variable("temperature"), "error fetching temperature data from simulator")

        env_data = temp_sensor.get_environment_data(env)
        self.assertEqual(env_data, env.get_environment_variable("temperature"), "error fetching temperature data from environment")

    def test_humidity_sensor(self):
        '''
        Test that humidity sensor is able to fetch data
        '''
        env = Environment(25.0, 60, 550)
        humidity_sensor = HumiditySensor(env)

        simulator_data = humidity_sensor.get_simulator_data()
        self.assertEqual(simulator_data, env.get_environment_variable("humidity"), "error fetching humidity data from simulator")

        env_data = humidity_sensor.get_environment_data(env)
        self.assertEqual(env_data, env.get_environment_variable("humidity"), "error fetching humidity data from environment")       

    def test_light_sensor(self):
        '''
        Test that light spectrum sensor is able to fetch data
        '''
        env = Environment(25.0, 60, 550)
        light_sensor = LightSensor(env)

        simulator_data = light_sensor.get_simulator_data()
        self.assertEqual(simulator_data, env.get_environment_variable("light"), "error fetching light spectrum data from simulator")

        env_data = light_sensor.get_environment_data(env)
        self.assertEqual(env_data, env.get_environment_variable("light"), "error fetching light spectrum data from environment")  

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

    def test_heater_invalid_input(self):
        '''
        Test if heater handles invalid parameter being passed to change_temp
        '''
        env = Environment(25.0, 60, 550)
        heater = Heater(env)

        with self.assertRaises(TypeError):
            heater.change_temp("x")

        # test heater being passed value out of boundaries
        heater.change_temp(100.0)
        self.assertEqual(env.get_environment_variable("temperature"), 40.0, "heater does not handle out-of-boundary input value")
        heater.change_temp(10.0)
        self.assertEqual(env.get_environment_variable("temperature"), 15.0, "heater does not handle out-of-boundary input value")

        # test if temperature is converted to float if it is passed in as integer
        heater.change_temp(20)
        self.assertEqual(env.get_environment_variable("temperature"), 20.0, 
                        "integer temperature value not converted to float in heater")

    def test_humidifier_invalid_input(self):
        '''
        Test if humidifier handles invalid parameter being passed to change_humidity
        '''
        env = Environment(25.0, 60, 550)
        humidifier = Humidifier(env)

        with self.assertRaises(TypeError):
            humidifier.change_humidity("x")

        # test humidifier being passed value out of boundaries
        humidifier.change_humidity(150)
        self.assertEqual(env.get_environment_variable("humidity"), 100, "humidifier does not handle out-of-boundary input value")
        humidifier.change_humidity(20)
        self.assertEqual(env.get_environment_variable("humidity"), 40, "humidifier does not handle out-of-boundary input value")

    def test_lights_invalid_input(self):
        '''
        Test if lights handle invalid parameter being passed to change_light
        '''
        env = Environment(25.0, 60, 550)
        lights = Lights(env)

        with self.assertRaises(TypeError):
            lights.change_light("x")

        # test lights being passed value out of boundaries
        lights.change_light(900)
        self.assertEqual(env.get_environment_variable("light"), 850, "lights do not handle out-of-boundary input value")
        lights.change_light(20)
        self.assertEqual(env.get_environment_variable("light"), 150, "lights do not handle out-of-boundary input value")

class TestActuatorActivation(unittest.TestCase):
    def test_difference_actuators_idle(self):
        '''
        Test if actuators stay inactive when user's setting is within acceptable range from 
        current environment reading
        '''
        env = Environment(25.0, 60, 550)
        sensors = initialize_sensors(env)
        actuators = initialize_actuators(env)

        env.set_user_settings(25.5, 61, 548)
        work(env, sensors, actuators, 1)
        self.assertEqual(env.get_environment_variable("temperature"), 25.0, 
                         "heater activated while temperature difference within acceptable range")
        self.assertEqual(env.get_environment_variable("humidity"), 60, 
                         "humidifier activated while humidity difference within acceptable range")
        self.assertEqual(env.get_environment_variable("light"), 550, 
                         "lights activated while light spectrum value within acceptable range")
        
    def test_difference_actuators_activate(self):
        '''
        Test if actuators activate when user's setting is out of acceptable range from 
        current environment reading
        '''
        env = Environment(25.0, 60, 550)
        sensors = initialize_sensors(env)
        actuators = initialize_actuators(env)

        # higher value
        env.set_user_settings(27.0, 70, 600)
        work(env, sensors, actuators, 1)
        self.assertEqual(env.get_environment_variable("temperature"), 27.0, 
                         "heater not activated when temperature difference out of acceptable range")
        self.assertEqual(env.get_environment_variable("humidity"), 70, 
                         "humidifier not activated when humidity difference out of acceptable range")
        self.assertEqual(env.get_environment_variable("light"), 600, 
                         "lights not activated when light spectrum value out of acceptable range")
        
        # lower value
        env.set_user_settings(20.0, 40, 500)
        work(env, sensors, actuators, 1)
        self.assertEqual(env.get_environment_variable("temperature"), 20.0, 
                         "heater not activated when temperature difference out of acceptable range")
        self.assertEqual(env.get_environment_variable("humidity"), 40, 
                         "humidifier not activated when humidity difference out of acceptable range")
        self.assertEqual(env.get_environment_variable("light"), 500, 
                         "lights not activated when light spectrum value out of acceptable range")
        
    def test_difference_actuators_boundaries(self):
        '''
        Test if actuators stay inactive when user's setting is on the boundary within acceptable 
        range from current environment reading
        '''
        env = Environment(25.0, 60, 550)
        sensors = initialize_sensors(env)
        actuators = initialize_actuators(env)

        # upper boundary
        env.set_user_settings(26.0, 62, 555)
        work(env, sensors, actuators, 1)
        self.assertEqual(env.get_environment_variable("temperature"), 25.0, 
                         "heater activated when temperature difference is upper boundary within acceptable range")
        self.assertEqual(env.get_environment_variable("humidity"), 60, 
                         "humidifier activated when humidity is upper boundary within acceptable range")
        self.assertEqual(env.get_environment_variable("light"), 550, 
                         "lights activated when light spectrum value is upper boundary acceptable range")
        
        # lower boundary
        env.set_user_settings(24.0, 58, 545)
        work(env, sensors, actuators, 1)
        self.assertEqual(env.get_environment_variable("temperature"), 25.0, 
                         "heater activated when temperature difference is lower boundary acceptable range")
        self.assertEqual(env.get_environment_variable("humidity"), 60, 
                         "humidifier activated when humidity difference is lower boundary acceptable range")
        self.assertEqual(env.get_environment_variable("light"), 550, 
                         "lights activated when light spectrum value is lower boundary acceptable range")

# class TestUserInput(unittest.TestCase):


if __name__ == '__main__':
    unittest.main()