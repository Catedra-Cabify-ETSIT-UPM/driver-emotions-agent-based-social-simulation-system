from DrivingTraits import *

def evaluateStress (self, stressOutcome):
    #Stress manifested as anxiety
    if stressOutcome == "Anxiety":
        self.speed.fast += 1
        self.acceleration.fast += 1
        self.steering.high += 1
        self.rt.high += 1

    #Stress manifested as anger
    elif stressOutcome == "Anger":
        self.speed.fast += 1
        self.acceleration.fast += 1
        self.braking.abrupt += 1
        self.steering.high += 1
        self.rt.low += 1

    #No stress case
    else:
        return

