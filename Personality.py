from DrivingTraits import *

#Big Five personality dimensions to determine driving styles: Extraversion, Agreeableness, Conscientiousness, Neuroticism, Openness

def evaluatePersonality(self, personality):
    #Personality values 
    extraversion = personality["Extraversion"]  
    agreeableness = personality["Agreeableness"]
    conscientiousness = personality["Conscientiousness"]
    neuroticism = personality["Neuroticism"]
    openness = personality["Openness"] 

    #Check reckless driving style 
    if (extraversion == 1 and agreeableness == 0 and conscientiousness == 0 and neuroticism == 1):
        self.speed.slow += 1
        self.speed.fast += 1
        self.acceleration.slow += 1
        self.acceleration.fast += 1
        self.braking.abrupt += 1
        self.steering.high += 1
        self.rt.high += 1

    #Check anxious driving style 
    elif (agreeableness == 0 and conscientiousness == 0 and neuroticism == 1 and openness == 1):
        self.speed.fast += 1
        self.acceleration.fast += 1
        self.steering.high += 1
        self.rt.high += 1

    #Check angry driving style 
    elif (agreeableness == 0 and conscientiousness == 0 and neuroticism == 1 and openness == 0):
        self.speed.fast += 1
        self.acceleration.fast += 1
        self.braking.abrupt += 1
        self.steering.high += 1
        self.rt.low += 1

    #Check careful driving style 
    elif (extraversion == 1 and agreeableness == 1 and conscientiousness == 1 and neuroticism == 0 and openness == 1):
        self.speed.appropiate += 1
        self.acceleration.appropiate += 1
        self.braking.gentle += 1
        self.steering.low += 1
        self.rt.low += 1

    #Default case
    else: 
        return 

