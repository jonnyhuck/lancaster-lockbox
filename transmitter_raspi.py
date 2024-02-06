"""
This is the Raspberry Pi part of the code for the 
"""
from serial import Serial
from os import path, listdir, system as os_system


def validate_input():
    """
    * How to respond to each number that is input
    """
    pass


# set the unlock code (needs to be the same as on the receiver)
UNLOCK_CODE = "hkaqBgsbRARY"

# clear the console
os_system('clear')

# infinite loop (allow multiple inputs)
while True:

    # start user output
    print(f"\nCAN YOU UNLOCK THE BOX?")
    print(f"Enter '/exit' or '/x', or use Ctrl+C to exit\n")

    # read in message from the user
    string_in = input("\nWhat is the number?\n")

    # end on /exit command
    if string_in in ["/exit", "/x"]:
        break

    # this is the location of the serial devices list
    serial_dev_dir = '/dev/serial/by-id'

    # verify it exists
    if path.isdir(serial_dev_dir):

        # get the list of serial devices
        serial_devices = listdir(serial_dev_dir)

        # make sure that at least one device is available
        if len(serial_devices) > 0:

            # get the path to the first available device
            serial_device_path = path.join(serial_dev_dir, serial_devices[0])

            # open serial interface
            serial = Serial(port=serial_device_path, baudrate=19200, timeout=0.5)

            # send the unlock code
            serial.write(bytes(UNLOCK_CODE, encoding='utf-8'))
        
        else:
            print("No serial device available")
            exit(1)
    else:
        print("No serial device connected")
        exit(1)