"""
This script is for the microbit that is plugged in to the Raspberry PI, acting as the radio transitter.

TODO: This must be run on one of the older microbits (with shiny surface) - the new ones (with matt 
    surface) give a Unicode Error because an empty bytestring is returned. This needs investigating.
"""

import radio
from microbit import uart, display

# initialise serial comms
uart.init(baudrate=19200)

# turn on the radio interface and config
radio.on()
radio.config(group=1)

# init message cache
messages = []

# infinite loop
while True:

    # try to read a line of serial
    msg = uart.readline()
    
    # if there is a message, convert to string and cache it
    if msg != None:        
        display.show("T")
        current = str(msg.upper(), 'UTF-8')

        # if it is the end (...$) compile and send it
        if current[-1] == "$":

            # append all but the 'end' tag to the cache
            messages.append(current[:-1])
            
            # compile the message and transmit, empty the cache
            radio.send("".join(messages))
            messages = []
            display.clear()
        
        # just append to the cache
        else:
            messages.append(current)