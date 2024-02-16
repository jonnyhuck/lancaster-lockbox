"""
This is the Raspberry Pi part of the code for the 
"""
from serial import Serial
from os import path, listdir, system as os_system


# set the unlock code (needs to be the same as on the receiver)
ANSWER = str(4783)              # this is what the user has to type in
UNLOCK_CODE = "hkaqBgsbRARY"    # this is what the microbit is listening for

# clear the console
os_system('clear')

# infinite loop (allow multiple inputs)
while True:

    # start user output
    print(f"\nCAN YOU UNLOCK THE BOX?")

    # read in message from the user
    string_in = input("\nEnter password?\n")

    # check answer
    if string_in != ANSWER:

        # incorrect - ask again
        print(f"\nINCORRECT.\n")
        continue

    # if correct, send unlock signal
    else:
        print(f"\nCORRECT.\n")

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
                serial.write(bytes(UNLOCK_CODE.upper() + "$", encoding='utf-8'))
            
            else:
                print("No serial device available")
                exit(1)
        else:
            print("No serial device connected")
            exit(1)