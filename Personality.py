from DrivingTraits import *
from numpy.random import choice

#Big Five personality dimensions to determine driving styles: Extraversion, Agreeableness, Conscientiousness, Neuroticism, Openness

def evaluatePersonality(self, personality):
    #Personality values 
    extraversion = int(personality["extraversion"])  
    agreeableness = int(personality["agreeableness"])
    conscientiousness = int(personality["conscientiousness"])
    neuroticism = int(personality["neuroticism"])
    openness = int(personality["openness"])

    #Check reckless driving style 
    if (extraversion == 1 and agreeableness == -1 and conscientiousness == -1 and neuroticism == 1 and openness == 0):
        if choice((True, False), 1, (0.6,0.4)):
            self.speed.fast += 1
            self.acceleration.fast += 1
            self.braking.abrupt += 1
            self.steering.high += 1
            self.rt.high += 1
        else:
            self.speed.slow += 1
            self.acceleration.slow += 1
            self.rt.low += 1
        return

    #Check anxious driving style 
    elif (extraversion == 0 and agreeableness == -1 and conscientiousness == -1 and neuroticism == 1 and openness == 1):
        #No clear association between anxious driving style and braking type
        self.speed.fast += 1
        self.acceleration.fast += 1
        self.steering.high += 1
        self.rt.high += 1
        return

    #Check angry driving style 
    elif (extraversion == 0 and agreeableness == -1 and conscientiousness == -1 and neuroticism == 1 and openness == -1):
        self.speed.fast += 1
        self.acceleration.fast += 1
        self.braking.abrupt += 1
        self.steering.high += 1
        #Angry driving style is supposed to help reduce response times because of increased driver attention, but speed can have the opposite effect on response times
        if choice((True, False)):
            self.rt.low += 1
        else:
            return
        return

    #Check careful driving style 
    elif (extraversion == 1 and agreeableness == 1 and conscientiousness == 1 and neuroticism == -1 and openness == 1):
        self.speed.appropiate += 1
        self.acceleration.appropiate += 1
        self.braking.gentle += 1
        self.steering.low += 1
        self.rt.low += 1
        return

    #Default case
    else: 
        return 

