"""
* This is installed on the microbit in the ammo box
"""

import radio
from microbit import display, sleep, pin1, button_a


def unlock():
    """
    * unlock the box for 2.5 seconds
    """
    pin1.write_digital(1)
    sleep(2500)
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

    # check button and unlock if pressed (for testing)
    if button_a.is_pressed():
        display.show("A")
        unlock()
    
    # try to read a message
    packet = radio.receive()
    if packet:
        display.show('R')
        
        # if the message is the unlock code...
        if packet.upper() == 'hkaqBgsbRARY'.upper():
            
            # ...then unlock!
            unlock()
            display.scroll("UNLOCKED!")
        
        # ...otherwise just display an X
        else:
            display.show('X')
            sleep(1000)
            display.clear()