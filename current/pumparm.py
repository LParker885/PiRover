#This code arms the ESC for the pump
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
import time


def arm():
    kit.servo[11].set_pulse_width_range(1000,2000)

    kit.servo[1].angle = 0
    time.sleep(2)
    kit.servo[1].angle = 180
    time.sleep(2)
    kit.servo[1].angle = 0
    time.sleep(2)
    kit.servo[1].angle = 10
    time.sleep(2)
    kit.servo[1].angle = 0 
