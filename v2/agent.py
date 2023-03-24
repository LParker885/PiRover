import numpy as np
#impot ros2

class DwayneJohnson:
    def __init__(self, topSpeed):
        
        
        #init ros2 cmd_vel publisher for left, right
        #init ros2 subscriber for data
        
        


        self.inputData=np.array([ 
         [ ], #lidar input 360 element array
        [], #accelerometer and gyro 6 element array
        [], #current wheel speeds 2-element array
        [], #x and y straight-line distance to target point - 2 element array
            
            ])
        
        self.goFast(0,0)
        
        self.enableGo = False

        pass

    def updateEnv(self,data):
        #gather data from ros2 data subscriber, put into data array - function may not be needed 
        pass

    def allowZip(self,enable):
        self.enableGo = enable
        pass

    def goFast(self,left, right):
        if(self.enableGo):

            #update ros2 cmd_vel publisher to match left, right
            pass
        else:
            pass
        pass

    def makePrediction(self):
        #run neuralnet to make prediction of how to gofast
        #goFast(neuralnetoutleft, neuralnetoutright)
        #return neuralnet confidence
        pass

    
