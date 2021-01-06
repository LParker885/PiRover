# a simple test to check that the pump is working and the valve servos work. 

from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
import time




kit.servo[11].set_pulse_width_range(1100,1500)
kit.servo[5].set_pulse_width_range(1500,2400)
kit.servo[4].set_pulse_width_range(1400,2400)

kit.servo[11].angle = 0
kit.servo[5].angle = 90
kit.servo[4].angle = 90
time.sleep(1)
kit.servo[5].angle = 180
kit.servo[11].angle = 30
time.sleep(1)
kit.servo[5].angle = 90
kit.servo[11].angle = 0
time.sleep(1)
kit.servo[5].angle = 0
kit.servo[11].angle = 40
time.sleep(1)
kit.servo[5].angle = 90
kit.servo[11].angle = 0
time.sleep(1)
kit.servo[4].angle = 180
kit.servo[11].angle = 30
time.sleep(1)
kit.servo[4].angle = 90
kit.servo[11].angle = 0
time.sleep(1)
kit.servo[4].angle = 0
kit.servo[11].angle = 30
time.sleep(1)
kit.servo[4].angle = 90
kit.servo[11].angle = 0
time.sleep(1)
kit.servo[5].angle = 180
kit.servo[11].angle = 30
time.sleep(1)
kit.servo[5].angle = 90
kit.servo[11].angle = 0
time.sleep(1)
kit.servo[5].angle = 0
kit.servo[11].angle = 40
time.sleep(1)
kit.servo[5].angle = 90
kit.servo[11].angle = 0

kit.servo[5].angle = 90
kit.servo[4].angle = 90
