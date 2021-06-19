from DrivingTraits import *

def evaluateStress (self, stressOutcome):
    #Stress manifested as anxiety
    if stressOutcome == "Anxiety":
        #No clear association between anxiety caused by stress and braking
        self.speed.fast += 1
        self.acceleration.fast += 1
        self.steering.high += 1
        self.rt.high += 1

    #Stress manifested as anger
    elif stressOutcome == "Anger":
        #RT not taken into account because anger caused by driving stress is more related with aggressive behaviours (low RT compensated with high speed)
        self.speed.fast += 1
        self.acceleration.fast += 1
        self.braking.abrupt += 1
        self.steering.high += 1

    #No stress case
    else:
        return

