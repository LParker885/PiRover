#this code is not yet updated for the new vehicle, but will be soon!
import RPi.GPIO as IO
import time
import atexit
from sense_hat import SenseHat


sense = SenseHat()
sense.clear()



IO.setmode(IO.BCM)
IO.setwarnings(False)



class Car:
    def __init__(self):
        IO.setup(9, IO.OUT)
        IO.setup(14, IO.OUT)
        IO.setup(17, IO.OUT)
        IO.setup(4, IO.OUT)
        IO.setup(11, IO.OUT)
        IO.setup(18, IO.OUT)
        IO.setup(7, IO.OUT)
        IO.setup(15, IO.OUT)
        IO.setup(21, IO.OUT)
        IO.output(21, IO.LOW)
        self.p1 = IO.PWM(14 , 1)
        self.p2 = IO.PWM(4 , 1)
        self.p3 = IO.PWM(18 , 1)
        self.p4 = IO.PWM(15 , 1)
        self.p1.start(0)
        self.p2.start(0)
        self.p3.start(0)
        self.p4.start(0)


    def motorsEnabled(self):
        IO.output(21, IO.HIGH)

    def motorsDisabled(self):
        IO.output(21, IO.LOW)

    def motorsOn(self):
        self.motorsEnabled()
        self.p1.ChangeDutyCycle(50)
        self.p2.ChangeDutyCycle(50)
        self.p3.ChangeDutyCycle(50)
        self.p4.ChangeDutyCycle(50)

    def motorsOff(self):
        self.motorsDisabled()
        self.p1.ChangeDutyCycle(0)
        self.p2.ChangeDutyCycle(0)
        self.p3.ChangeDutyCycle(0)
        self.p4.ChangeDutyCycle(0)



    def goSpeed(self,speed1,speed2):
        self.motorsOn()
        self.p1.ChangeFrequency(speed1)
        self.p2.ChangeFrequency(speed1)
        self.p3.ChangeFrequency(speed2)
        self.p4.ChangeFrequency(speed2)

    def goTank(self,speed1,speed2, direction1, direction2):
        if direction1 == 1:
            IO.output(9, IO.LOW)
            IO.output(17, IO.LOW)
        else:
            IO.output(9, IO.HIGH)
            IO.output(17, IO.HIGH)
        if direction2 == 1:
            IO.output(7, IO.LOW)
            IO.output(11, IO.LOW)
        else:
            IO.output(7, IO.HIGH)
            IO.output(11, IO.HIGH)
        self.goSpeed(speed1, speed2)

    def getSteer(self):
        o = sense.get_orientation()
        pitch = round(o["pitch"])
        roll = round(o["roll"])
        yaw = round(o["yaw"])
        return yaw

    def goSteer(self, direction, speed):
        if(direction == 2):
            self.goTank(speed,speed,0,1)
        elif (direction == 1):
            self.goTank(speed,speed,1,0)


