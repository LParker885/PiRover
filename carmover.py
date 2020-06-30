import time
from carclass import Car


c = Car()


while 1:


    f = open("/var/www/html/input.txt", "r")
    xs = f.readline().rstrip('\n')
    ys =  f.readline().rstrip('\n')
    th = f.readline().rstrip('\n')
    turn = f.readline().rstrip('\n')
    go = f.readline().rstrip('\n')
    f.close()


    if(xs.isnumeric() and xs != '' and ys.isnumeric() and ys != '' and th.isnumeric() and th != '' and turn.isnumeric() and turn != '' and go.isnumeric() and go != ''):
        xs=max(0,min(int(xs),180))
        ys=max(0,min(int(ys),180))
        th=max(0,min(int(th),700))
        turn=max(0,min(int(turn),2))
        go=max(0,min(int(go),2))
        if(go == 1 and th > 0):
            c.goTank(th,th,1,1)
        elif(go == 2 and th > 0):
            c.goTank(th,th,0,0)
        elif((turn == 1 or turn == 2) and th > 0):
            c.goSteer(turn, th)
        else:
            c.motorsOff()


    time.sleep(0.01)