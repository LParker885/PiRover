import RPi.GPIO as IO
import time
import board
import atexit
from adafruit_servokit import ServoKit
from adafruit_motorkit import MotorKit
Motor = MotorKit(i2c=board.I2C())
Servos = ServoKit(channels=16)


class Car:
    def __init__(self):
        Servos.servo[0].set_pulse_width_range(1100,2400)
        Servos.servo[2].set_pulse_width_range(900,2400)
        Servos.servo[11].set_pulse_width_range(1000,1500)
        Servos.servo[5].set_pulse_width_range(1350,2400)
        Servos.servo[4].set_pulse_width_range(1400,2400)
        Motor.motor2.throttle = 0
        #self.armPump()


    def armPump(self):
        Servos.servo[11].angle = 0
        time.sleep(2)
        Servos.servo[11].angle = 180
        time.sleep(1)
        Servos.servo[11].angle = 0
        time.sleep(2)

    def stop(self):
        Motor.motor2.throttle = 0
        Servos.servo[2].angle = 90

    def drive(self,heading,throttle,turntablethrottle,teim):
        Motor.motor2.throttle = throttle
        Servos.servo[0].angle = heading
        Servos.servo[2].angle = turntablethrottle
        time.sleep(teim)
        self.stop()



    def armMove(self,s,e,h,t,l):
        Servos.servo[5].angle = ((90*(-1*s))+90)
        Servos.servo[4].angle = (90*(e))+90
        Servos.servo[6].angle = (90*(h))+90
        Servos.servo[11].angle = t*(180/100)
        time.sleep(l)
        Servos.servo[11].angle = 0
        Servos.servo[5].angle = 90
        Servos.servo[4].angle = 90
        Servos.servo[6].angle = 90

car = Car()

car.drive(90,-0.5,90,3)



#car.armMove(-1,1,0,25,2)
#car.armMove(1,-1,0,50,2)
#car.armMove(0,1,0,25,2)
#car.armMove(0,-1,0,30,2)



