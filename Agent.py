from mesa import Agent, Model 
from DrivingTraits import *
from Emotions import evaluateEmotions
from Personality import evaluatePersonality
from Stress import evaluateStress
from DrivingStyles import *
from AccidentProbability import *

class DriverAgent(Agent):

    #Initializes DriverAgent object 
    def __init__(self, unique_id, model, emotionValues, personalityValues, stressValue):
        super().__init__(unique_id, model)
        #An agent is characterized by emotions, personality traits and stress
        #Stress, distractions can vary on each agent's step but emotions and personality traits remain constant 
        #Emotions
        self.emotions = emotionValues
        #Personality 
        self.personality = personalityValues
        #Stress
        self.stress = stressValue
        #Distraction
        self.distraction = 0
        #Driving traits
        self.speed = Speed()
        self.acceleration = Acceleration()
        self.braking = Braking()
        self.steering = SteeringWheel()
        self.rt = ResponseTime()
        #Accident rate
        self.accidentRate = 0
        #First emotion/personality/stress evaluation
        evaluateEmotions(self, self.emotions)
        evaluatePersonality(self, self.personality)
        evaluateStress(self, self.stress)

        
    def getEmotions(self, emotionValues):
        emotion_names = ["Happiness", "Fear", "Anger", "Anxiety"]
        emotions = dict(zip(emotion_names, emotionValues))
        return emotions

    def getPersonality(self, personalityValues):
        personality_names = ["Extraversion", "Agreeableness", "Conscientiousness", "Neuroticism", "Openness"]
        personality = dict(zip(personality_names, personalityValues))
        return personality  

    def step(self):
        #The agent's step is defined here.
        evaluateEmotions(self, self.emotions)
        evaluatePersonality(self, self.personality)
        evaluateStress(self, self.stress)

        self.speed.dominant = getSpeed(self, self.speed)
        self.acceleration.dominant = getAcceleration(self, self.acceleration)
        self.braking.dominant = getBraking(self, self.braking)
        self.steering.dominant = getSteering(self, self.steering)
        self.rt.dominant = getRT(self, self.rt)
        #drivingStyle = setDrivingStyle(self, self.speed, self.acceleration, self.braking, self.steering, self.rt)

        # if ("Speed FAST" in drivingStyle) or ("Acceleration FAST" in drivingStyle):
        #     self.accidentRate = getSpeedFrequency() 
        # elif "Steering HIGH" in drivingStyle:
        #     self.accidentRate = getSteeringFrequency()
        # elif "RT HIGH" in drivingStyle:
        #     self.accidentRate = getRTFrequency()
        # else: 
        #     pass
        #VARIABILITY
        pass


