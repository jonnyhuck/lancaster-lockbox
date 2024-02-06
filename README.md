# Lancaster Air Cadets Lockbox Game
This repository is the code for the console interface for a game that requires the players to work out a passcode to open a box. 

Also required is a Raspberry Pi and 2x BBC MicroBits.

The Raspberry Pi should have [`transmitter_raspi.py`](./transmitter_raspi.py)  running, and be attached by USB to a Raspberry Pi with [`transmitter_microbit.py`](./transmitter_microbit.py) running. The other microbit is attached to the box to control the electronic lock, and should have [`receiver_microbit.py`](./transmitter_microbit.py) running.
