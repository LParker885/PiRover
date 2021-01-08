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
    def throttleGo(t,g):
        if g == 0:
            Motor.motor2.throttle = 0
        if g == 1:
            Motor.motor2.throttle = -t
        if g == 2:
            Motor.motor2.throttle = t
    def headingGo(h):
        Servos.servo[0].angle = h
    def turntableGo(a):
        Servos.servo[2].angle = a
        
    def driveGo(self,heading,throttle,turntablethrottle):
        Motor.motor2.throttle = throttle
        Servos.servo[0].angle = heading
        Servos.servo[2].angle = turntablethrottle
        
    def drive(self,heading,throttle,turntablethrottle,teim):
        self.driveGo()
        time.sleep(teim)
        self.stop()
    def moveCam(self,x,y):
        #move the servos

    def armGo(self,s,e,h,t,l):
        Servos.servo[5].angle = ((90*(-1*s))+90)
        Servos.servo[4].angle = (90*(e))+90
        Servos.servo[6].angle = (90*(h))+90
        Servos.servo[11].angle = t*(180/100)
    def jointGo(joint,move,speed):
        if joint == 1:
            Servos.servo[5].angle = ((90*(-1*s))+90)
        if joint == 2:
            Servos.servo[4].angle = (90*(e))+90
        if joint == 3:
            Servos.servo[6].angle = (90*(h))+90
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
         f = open("/var/www/html/input.txt", "r")
         xc = f.readline().rstrip('\n')
         yc =  f.readline().rstrip('\n')
         th = f.readline().rstrip('\n')
         tu =  f.readline().rstrip('\n')
         go = f.readline().rstrip('\n')
         tt =  f.readline().rstrip('\n')
         j1 = f.readline().rstrip('\n')
         j2 =  f.readline().rstrip('\n')
         j3 = f.readline().rstrip('\n')
         at = f.readline().rstrip('\n')
         f.close()
         if(xs.isnumeric() and xs != ''):
            if(ys.isnumeric() and ys != ''):
                self.moveCam(xs,ys)
         if(th.isnumeric() and th != ''):
            if(go.isnumeric() and go != ''):
                self.throttleGo(th,go)
         if(tu.isnumeric() and tu != ''):
            self.throttleGo(tu)
         if(tt.isnumeric() and tt != ''):
            self.throttleGo(tt)
         if(j1.isnumeric() and j1 != ''):
            if(at.isnumeric() and at != ''):
                self.jointGo(1,j1,at)
         if(j2.isnumeric() and j2 != ''):
            if(at.isnumeric() and at != ''):
                self.jointGo(2,j2,at)
         if(j3.isnumeric() and j3 != ''):
            if(at.isnumeric() and at != ''):
                self.jointGo(3,j3,at)
         
         
        
#possible ranges of paramaters!        
#For the drive function: (0-180,-1-1,0-180)
#for the arm function: (-1-1,-1-1,-1-1,0-100)
   


