#This class implements the driving behaviour characterization through the analysis of drivers' emotions

from DrivingTraits import *
from numpy.random import choice


def evaluateEmotions(self, emotions):
    #Evaluate happiness
    if int(emotions["happiness"]) == 1:
        self.speed.appropiate += 1 
        self.acceleration.appropiate += 1
        self.braking.gentle += 1
        self.steering.low += 1
        self.rt.high += 1
        return

    #Evaluate fear
    elif int(emotions["fear"]) == 1:
        #No clear association between fear and steering
        self.speed.slow += 1
        self.acceleration.slow += 1 
        self.braking.abrupt += 1
        self.rt.low += 1
        return

    #Evaluate anger
    elif int(emotions["anger"]) == 1:
        self.speed.fast += 1
        self.acceleration.fast += 1
        self.braking.abrupt += 1
        self.steering.high += 1
        if choice((True, False)):
            self.rt.low += 1
        else:
            return
        return

    #Evaluate anxiety
    elif int(emotions["anxiety"]) == 1:
        #No clear association between anxiety and braking type
        self.speed.fast += 1
        self.acceleration.fast += 1
        self.steering.high += 1
        self.rt.high += 1
        return

    #Default case
    else:
        return