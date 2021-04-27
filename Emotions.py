#This class implements the driving behaviour characterization through the analysis of drivers' emotions

from DrivingTraits import *

def evaluateEmotions(self, emotions):
    #Evaluate happyness
    if emotions[0] == 1:
        Speed.SLOW = 0
        Speed.APPROPIATE = 1 
        Speed.FAST = 0
        Acceleration.SLOW = 0 
        Acceleration.APPROPIATE = 1
        Acceleration.FAST = 0
        Braking.GENTLE = 1
        Braking.ABRUPT = 0
        SteeringWheel.LOW = 1
        SteeringWheel.HIGH = 0
        ResponseTime.LOW = 0
        ResponseTime.HIGH = 1
    #Evaluate fear
    elif emotions[1] == 1:
        Speed.SLOW = 1
        Speed.APPROPIATE = 0 
        Speed.FAST = 0
        Acceleration.SLOW = 1 
        Acceleration.APPROPIATE = 0
        Acceleration.FAST = 0
        Braking.GENTLE = 0
        Braking.ABRUPT = 1
        SteeringWheel.LOW = 1
        SteeringWheel.HIGH = 0
        ResponseTime.LOW = 1
        ResponseTime.HIGH = 0
    #Evaluate anger
    elif emotions[2] == 1:
        Speed.SLOW = 0
        Speed.APPROPIATE = 0 
        Speed.FAST = 1
        Acceleration.SLOW = 0 
        Acceleration.APPROPIATE = 0
        Acceleration.FAST = 1
        Braking.GENTLE = 0
        Braking.ABRUPT = 1
        SteeringWheel.LOW = 0
        SteeringWheel.HIGH = 1
        ResponseTime.LOW = 1
        ResponseTime.HIGH = 0
    #Evaluate anxiety
    elif emotions[3] == 1:
        Speed.SLOW = 0
        Speed.APPROPIATE = 0 
        Speed.FAST = 1
        Acceleration.SLOW = 0 
        Acceleration.APPROPIATE = 0
        Acceleration.FAST = 1
        Braking.GENTLE = 0
        Braking.ABRUPT = 1
        SteeringWheel.LOW = 0
        SteeringWheel.HIGH = 1
        ResponseTime.LOW = 0
        ResponseTime.HIGH = 1
    #Default case
    else:
        Speed.SLOW = 0
        Speed.APPROPIATE = 0 
        Speed.FAST = 0
        Acceleration.SLOW = 0 
        Acceleration.APPROPIATE = 0
        Acceleration.FAST = 0
        Braking.GENTLE = 0
        Braking.ABRUPT = 0
        SteeringWheel.LOW = 0
        SteeringWheel.HIGH = 0
        ResponseTime.LOW = 0
        ResponseTime.HIGH = 0