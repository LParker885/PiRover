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
        Servos.servo[0].set_pulse_width_range(1000,2400)
        Servos.servo[2].set_pulse_width_range(900,2400)
        Servos.servo[11].set_pulse_width_range(1000,1500)
        Servos.servo[5].set_pulse_width_range(1350,2400)
        Servos.servo[4].set_pulse_width_range(1400,2300)
        Servos.servo[6].set_pulse_width_range(1400,2400)
        Servos.servo[15].set_pulse_width_range(300,2400)
        Servos.servo[14].set_pulse_width_range(400,2400)
        Motor.motor2.throttle = 0


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
    def throttleGo(self,t,g):
        if g == 0:
            Motor.motor2.throttle = 0
        if g == 1:
            Motor.motor2.throttle = -t
        if g == 2:
            Motor.motor2.throttle = t
    def headingGo(self,h):
        Servos.servo[0].angle = 90*h
    def turntableGo(self,a):
        if a == 0:
            Servos.servo[2].angle = 90
        if a == 1:
            Servos.servo[2].angle = 100
        if a == 2:
            Servos.servo[2].angle = 80

    def driveGo(self,heading,throttle,turntablethrottle):
        Motor.motor2.throttle = throttle
        Servos.servo[0].angle = heading
        Servos.servo[2].angle = turntablethrottle

    def drive(self,heading,throttle,turntablethrottle,teim):
        self.driveGo()
        time.sleep(teim)
        self.stop()
    def moveCam(self,x,y):
        Servos.servo[14].angle = y
        Servos.servo[15].angle = 180-x
        time.sleep(0.01)

    def armGo(self,s,e,h,t,l):
        Servos.servo[5].angle = ((90*(-1*s))+90)
        Servos.servo[4].angle = (90*(e))+90
        Servos.servo[6].angle = (90*(h))+90
        Servos.servo[11].angle = t*(180/100)
    def jointGo(self,joint,move,speed):
        if joint == 1:
            if move == 0:
                Servos.servo[6].angle = 90
            if move == 1:
                Servos.servo[6].angle = 180
            if move == 2:
                Servos.servo[6].angle = 0
        if joint == 2:
            if move == 0:
                Servos.servo[5].angle = 90
            if move == 1:
                Servos.servo[5].angle = 0
            if move == 2:
                Servos.servo[5].angle = 180
        if joint == 3:
            if move == 0:
                Servos.servo[4].angle = 90
            if move == 1:
                Servos.servo[4].angle = 0
            if move == 2:
                Servos.servo[4].angle = 180

        Servos.servo[11].angle = speed*(180/100)

    def armStop(self):
        Servos.servo[11].angle = 0
        Servos.servo[5].angle = 90
        Servos.servo[4].angle = 90
        Servos.servo[6].angle = 90

    def armMove(self,s,e,h,t,l):
        self.armGo(s,e,h,t,l)
        time.sleep(l)
        Servos.servo[11].angle = 0
        Servos.servo[5].angle = 90
        Servos.servo[4].angle = 90
        Servos.servo[6].angle = 90
    def moveFromFile(self):
        f = open("/mnt/ramdisk/input.txt", "r")
        xs = f.readline().rstrip('\n')
        ys =  f.readline().rstrip('\n')
        th = f.readline().rstrip('\n')
        tu =  f.readline().rstrip('\n')
        go = f.readline().rstrip('\n')
        tt =  f.readline().rstrip('\n')
        j1 = f.readline().rstrip('\n')
        j2 =  f.readline().rstrip('\n')
        j3 = f.readline().rstrip('\n')
        at = f.readline()
        f.close()
        if(xs.isnumeric() and xs != ''):
           if(ys.isnumeric() and ys != ''):
               self.moveCam(int(xs),int(ys))
        if(th.isnumeric() and th != ''):
           if(go.isnumeric() and go != ''):
               self.throttleGo(int(th)/100,int(go))
        if(tu.isnumeric() and tu != ''):
           self.headingGo(int(tu))
        if(tt.isnumeric() and tt != ''):
           self.turntableGo(max(0,min(int(tt),180)))
        if(j1.isnumeric() and j1 != ''):
           if(at.isnumeric() and at != '' and int(at) <= 100):
               self.jointGo(1,max(0,min(int(j1),180)),int(at))
        if(j2.isnumeric() and j2 != ''):
           if(at.isnumeric() and at != '' and int(at) <= 100):
               self.jointGo(2,max(0,min(int(j2),180)),int(at))
        if(j3.isnumeric() and j3 != ''):
           if(at.isnumeric() and at != '' and int(at) <= 100):
               self.jointGo(3,max(0,min(int(j3),180)),int(at))


car = Car()
#car.armPump()
while 1:

    car.moveFromFile()


#possible ranges of paramaters!
#For the drive function: self.drive(0-180,-1-1,0-180,time in seconds)
#for the arm function: self.armGo(-1-1,-1-1,-1-1,0-100,time in seconds)