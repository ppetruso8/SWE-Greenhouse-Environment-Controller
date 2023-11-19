''' main application, launching UI, function for processing data '''
def main():
    # from sensors.py
    initialize_sensors()
    # from actuators.py
    initialize_actuators()
    # from gui.py
    launch_gui()
    # main loop 
    work()

def work():
    pass

if __name__ == "__main__":
    main()