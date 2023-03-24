# PiRover

As of 1/13/2021 this code works, with as many bugs out as I can find. Yay!

The vehicle itself is a Rpi 4 powered car, with a two-joint pneumatic excavator-style arm and pneumatic bucket attached. 
It has a typical differential back 2-wheel drive, powered by a single Lego XL motor. The front steering is a servo-driven rack and pinion. There is also a servo-driven turntable which has the upper body, arm, and electronics mounted to it lumped in with the drive controls. 

I should probably mention that the robot is built out of legos because they are easy to build really complicated stuff with in fairly short amounts of time, and with no 3d printing or nonsense like that. 

Implementation notes / bugs fixed:
Put input.txt in a ramdisk directory. This saved the SD card, got rid of (most) of the servo jitters and just sped things up in general. 
Gave plenty of power to the servo board. Running it through a dedicated 5V transformer as opposed to the pi 5v sipply meant that the servos did not flip out when the pneumatic pump engaged. 
Added a bunch of filtering along the user -> movement pipeline, to keep out errors from inputs out of range, characters uninterpretable as integers, etc. 
Switched the coupling on the pump motor from a solid coupling to a universal joint to eliminate (most) of the weeble-wobbles that turned into nasty vibration at high speeds. 

