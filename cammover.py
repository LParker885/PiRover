from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

while 1:
    f = open("/var/www/html/input.txt", "r")
    xs = f.readline().rstrip('\n')
    ys =  f.readline().rstrip('\n')

    f.close()
    if(xs.isnumeric() and xs != ''):
        xs=max(0,min(int(xs),180))
        kit.servo[14].angle = 180-xs

    if(ys.isnumeric() and ys != ''):
        ys=max(0,min(int(ys),180))
        kit.servo[15].angle = ys