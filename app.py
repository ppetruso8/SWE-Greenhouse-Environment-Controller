''' 
Main Greenhouse Environment Controller code.
Responsible for launching UI, processing data, and adjusting actuators
'''

from sensors import initialize_sensors

def main():
    # from actuators.py
    #initialize_actuators()
    # from gui.py
    #launch_gui()
    
    # main loop 
    work()

def work():
    #while True:
    # get sensors in dictionary
    sensors = initialize_sensors()
    temperature_data = sensors["temperature"].get_data()
    humidity_data = sensors["humidity"].get_data()
    light_data = sensors["light"].get_data()
    print(temperature_data, humidity_data, light_data)
    

if __name__ == "__main__":
    main()