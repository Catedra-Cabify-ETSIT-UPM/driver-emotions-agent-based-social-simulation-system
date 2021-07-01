from DrivingTraits import *
from numpy.random import choice
import configparser

#Big Five personality dimensions to determine driving styles: Extraversion, Agreeableness, Conscientiousness, Neuroticism, Openness

def getSteps():
    config = configparser.ConfigParser()
    config.read('general.ini')
    simSteps = int(config["SIMULATION STEPS"]["steps"])
    return simSteps


def evaluatePersonality(self, personality):
    #Personality values 
    extraversion = int(personality["extraversion"])  
    agreeableness = int(personality["agreeableness"])
    conscientiousness = int(personality["conscientiousness"])
    neuroticism = int(personality["neuroticism"])
    openness = int(personality["openness"])
    steps = getSteps()
    contribution = steps/3

    #Check reckless driving style 
    if (extraversion == 1 and agreeableness == -1 and conscientiousness == -1 and neuroticism == 1 and openness == 0):
        if choice((True, False), 1, (0.6,0.4)):
            self.speed.fast += contribution
            self.acceleration.fast += contribution
            self.braking.abrupt += contribution
            self.steering.high += contribution
            self.rt.high += contribution
        else:
            self.speed.slow += contribution
            self.acceleration.slow += contribution
            self.rt.low += contribution
        return

    #Check anxious driving style 
    elif (extraversion == 0 and agreeableness == -1 and conscientiousness == -1 and neuroticism == 1 and openness == 1):
        #No clear association between anxious driving style and braking type
        self.speed.fast += contribution
        self.acceleration.fast += contribution
        self.steering.high += contribution
        self.rt.high += contribution
        return

    #Check angry driving style 
    elif (extraversion == 0 and agreeableness == -1 and conscientiousness == -1 and neuroticism == 1 and openness == -1):
        self.speed.fast += contribution
        self.acceleration.fast += contribution
        self.braking.abrupt += contribution
        self.steering.high += contribution
        #Angry driving style is supposed to help reduce response times because of increased driver attention, but speed can have the opposite effect on response times
        if choice((True, False)):
            self.rt.low += contribution
        else:
            return
        return

    #Check careful driving style 
    elif (extraversion == 1 and agreeableness == 1 and conscientiousness == 1 and neuroticism == -1 and openness == 1):
        self.speed.appropriate += contribution
        self.acceleration.appropriate += contribution
        self.braking.gentle += contribution
        self.steering.low += contribution
        self.rt.low += contribution
        return

    #Default case
    else: 
        return 

