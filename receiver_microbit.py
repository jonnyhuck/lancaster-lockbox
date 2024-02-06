"""
This is a boilerplate radio receiver - all you should need to do is
    replace the 'pass' line in the unlock() method with whatever you 
    need to do to deactivate the lock and we should be done!!

This is installed on the YELLOW microbit
"""

import radio
from microbit import display, sleep, pin1

def unlock():
    """
    Validate that the number is correct
    """
    pin1.write_digital(1)
    sleep(5000)
    pin1.write_digital(0)


# init display (just to show that it's working)
display.scroll("LOCKED!")
display.clear()
    
# turn on the radio interface
radio.on()

# set radio group
radio.config(group=1)

# infinite loop
while True:

    # try to read a message
    packet = radio.receive()
    if packet:
        display.show('R')
        
        # if the message is the unlock code...
        if packet.upper() == 'hkaqBgsbRARY'.upper():
            
            # ...then unlock!
            display.scroll("UNLOCKED!")
            unlock()
        
        # ...otherwise just display an X
        else:
            display.show('X')
            sleep(1000)
            display.clear()