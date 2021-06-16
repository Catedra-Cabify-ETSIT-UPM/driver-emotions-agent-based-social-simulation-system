#This class implements the driving behaviour characterization through the analysis of drivers' emotions

from DrivingTraits import *

def evaluateEmotions(self, emotions):
    #Evaluate happyness
    if emotions["Happyness"] == 1:
        self.speed.appropiate += 1 
        self.acceleration.appropiate += 1
        self.braking.gentle += 1
        self.steering.low += 1
        self.rt.high += 1
    #Evaluate fear
    elif emotions["Fear"] == 1:
        self.speed.slow += 1
        self.acceleration.slow += 1 
        self.braking.abrupt += 1
        self.steering.low += 1
        self.rt.low += 1
    #Evaluate anger
    elif emotions["Anger"] == 1:
        self.speed.fast += 1
        self.acceleration.fast += 1
        self.braking.abrupt += 1
        self.steering.high += 1
        self.rt.low += 1
    #Evaluate anxiety
    elif emotions["Anxiety"] == 1:
        self.speed.fast += 1
        self.acceleration.fast += 1
        self.braking.abrupt += 1
        self.steering.high += 1
        self.rt.high += 1
    #Default case
    else:
        return