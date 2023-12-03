'''testing and validation'''
import unittest
from unittest import mock
from controller import Environment, initialize_actuators, initialize_sensors, manage_environment
from actuators import Heater, Humidifier, Lights
from gui import initialize_gui, display_warning

class TestGettingEnvironment(unittest.TestCase):
    '''
    Class containing tests for the get_environment_variable method
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
        
class TestHeaterChangeTemp(unittest.TestCase):
    '''
    Class containing tests for the change_temp method of heater
    '''
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

class TestHumidifierChangeHumidity(unittest.TestCase):
    '''
    Class containing tests for change_humidity method for humidifier
    '''
    def setUp(self) -> None:
        self.env = Environment(25.0, 60, 550)
        self.humidifier = Humidifier(self.env) 

    def test_p1(self):
        with self.assertRaises(TypeError):
            self.humidifier.change_humidity("x")

    def test_p2(self):
        self.env.set_environment("humidity", 40)
        self.humidifier.change_humidity(35)
        self.assertEqual(self.env.get_environment_variable("humidity"), 40)

    def test_p3(self):
        self.env.set_environment("humidity", 65)

        with mock.patch('random.uniform', return_value=63):
           self.humidifier.change_humidity(64)
           self.assertEqual(self.env.get_environment_variable("humidity"), 64)

    def test_p4(self):
        self.env.set_environment("humidity", 64)

        with mock.patch('random.uniform', return_value=66):
           self.humidifier.change_humidity(65)
           self.assertEqual(self.env.get_environment_variable("humidity"), 65)

    def test_p5(self):
        self.env.set_environment("humidity", 99)

        with mock.patch('random.uniform', return_value=101):
            self.humidifier.change_humidity(110)
            self.assertEqual(self.env.get_environment_variable("humidity"), 100)

class TestLightsChangeLight(unittest.TestCase):
    '''
    Class containing tests for change_light method for lights
    '''
    def setUp(self) -> None:
        self.env = Environment(25.0, 60, 550)
        self.lights = Lights(self.env) 

    def test_p1(self):
        with self.assertRaises(TypeError):
            self.lights.change_light("x")

    def test_p2(self):
        self.env.set_environment("light", 150)
        self.lights.change_light(100)
        self.assertEqual(self.env.get_environment_variable("light"), 150)

    def test_p3(self):
        self.env.set_environment("light", 600)

        with mock.patch('random.uniform', return_value=596):
           self.lights.change_light(598)
           self.assertEqual(self.env.get_environment_variable("light"), 598)

    def test_p4(self):
        self.env.set_environment("light", 600)

        with mock.patch('random.uniform', return_value=605):
           self.lights.change_light(603)
           self.assertEqual(self.env.get_environment_variable("light"), 603)

    def test_p5(self):
        self.env.set_environment("light", 848)

        with mock.patch('random.uniform', return_value=853):
            self.lights.change_light(852)
            self.assertEqual(self.env.get_environment_variable("light"), 850)

class TestDisplayWarning(unittest.TestCase):
    '''
    Class containing tests for the display_warning method of gui
    '''
    def setUp(self) -> None:
        self.gui = initialize_gui()

    def test_p1(self):
        display_warning(self.gui["warning_label_temperature"],"temperature", "high")
        self.gui["root"].update()
        self.assertEqual(self.gui["warning_label_temperature"].cget("text"), "Warning: the temperature is too high\n")

    def test_p2(self):
        display_warning(self.gui["warning_label_temperature"], "temperature", "low")
        self.gui["root"].update()
        self.assertEqual(self.gui["warning_label_temperature"].cget("text"), "Warning: the temperature is too low\n")
    
    def test_p3(self):
        display_warning(self.gui["warning_label_temperature"], "temperature", "good")
        self.gui["root"].update()
        self.assertEqual(self.gui["warning_label_temperature"].cget("text"), "")

    def test_p4(self):
        display_warning(self.gui["warning_label_humidity"], "humidity", "high")
        self.gui["root"].update()
        self.assertEqual(self.gui["warning_label_humidity"].cget("text"), "Warning: the humidity is too high\n")

    def test_p5(self):
        display_warning(self.gui["warning_label_humidity"], "humidity", "low")
        self.gui["root"].update()
        self.assertEqual(self.gui["warning_label_humidity"].cget("text"), "Warning: the humidity is too low\n")

    def test_p6(self):
        display_warning(self.gui["warning_label_humidity"], "humidity", "good")
        self.gui["root"].update()
        self.assertEqual(self.gui["warning_label_humidity"].cget("text"), "")

    def test_p7(self):
        with self.assertRaises(ValueError):
            display_warning(self.gui["warning_label_humidity"], "moisture", "good")
            self.gui["root"].update()

    def test_p8(self):
        display_warning(self.gui["warning_label_light"], "light", "high")
        self.gui["root"].update()
        self.assertEqual(self.gui["warning_label_light"].cget("text"), "Warning: the light is too strong\n")

    def test_p9(self):
        display_warning(self.gui["warning_label_light"], "light", "low")
        self.gui["root"].update()
        self.assertEqual(self.gui["warning_label_light"].cget("text"), "Warning: the light is too weak\n")

    def test_p8(self):
        display_warning(self.gui["warning_label_light"], "light", "good")
        self.gui["root"].update()
        self.assertEqual(self.gui["warning_label_light"].cget("text"), "")

class TestManageEnvironment(unittest.TestCase):
    '''
    Class containing tests for the manage_environment function of controller
    '''
    def setUp(self) -> None:
        self.env = Environment(25.0, 60, 550)
        self.sensors = initialize_sensors(self.env)
        self.actuators = initialize_actuators(self.env) 
        self.gui = initialize_gui()

    def test_p1(self):
        manage_environment(self.env, self.sensors, self.actuators, self.gui, 0)

        self.assertEqual(self.env.get_environment(), {'temperature': 25.0, 'humidity': 60, 'light': 550})
    
    def test_p2(self):
        self.env.set_environment("temperature", 28.0)
        self.env.set_environment("humidity", 82)
        self.env.set_environment("light", 705)

        manage_environment(self.env, self.sensors, self.actuators, self.gui, 1)

        self.assertLessEqual(self.env.get_environment_variable("temperature"), 27.0)
        self.assertLessEqual(self.env.get_environment_variable("humidity"), 80)
        self.assertLessEqual(self.env.get_environment_variable("light"), 700)

    def test_p3(self):
        self.env.set_environment("temperature", 20.0)
        self.env.set_environment("humidity", 63)
        self.env.set_environment("light", 595)

        manage_environment(self.env, self.sensors, self.actuators, self.gui, 1)
        
        self.assertGreaterEqual(self.env.get_environment_variable("temperature"), 21.0)
        self.assertGreaterEqual(self.env.get_environment_variable("humidity"), 65)
        self.assertGreaterEqual(self.env.get_environment_variable("light"), 600)

    def test_p4(self):
        self.env.set_environment("temperature", 25.0)
        self.env.set_environment("humidity", 70)
        self.env.set_environment("light", 650)
        manage_environment(self.env, self.sensors, self.actuators, self.gui, 1)
        
        self.assertTrue(self.env.get_environment_variable("temperature") >= 21.0 
                        and self.env.get_environment_variable("temperature") <= 27.0)
        self.assertTrue(self.env.get_environment_variable("humidity") >= 65
                        and self.env.get_environment_variable("humidity") <= 80)
        self.assertTrue(self.env.get_environment_variable("light") >= 600
                        and self.env.get_environment_variable("light") <= 700)

if __name__ == '__main__':
    unittest.main()