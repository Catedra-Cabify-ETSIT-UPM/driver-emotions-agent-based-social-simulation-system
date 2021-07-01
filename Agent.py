from mesa import Agent, Model 
from DrivingTraits import *
from Emotions import evaluateEmotions
from Personality import evaluatePersonality
from Stress import evaluateStress
from DrivingStyles import *
from AccidentProbability import *
from numpy.random import choice

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
        self.accidentProbability = 0
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
        #Emotion contribution
        evaluateEmotions(self, self.emotions)
        #Stress contribution
        evaluateStress(self, self.stress)

        #Characterization of driving styles
        self.speed.dominant, speedMaxValue = getSpeed(self, self.speed)
        self.acceleration.dominant, _ = getAcceleration(self, self.acceleration)
        self.braking.dominant, _  = getBraking(self, self.braking)
        self.steering.dominant, steeringMaxValue  = getSteering(self, self.steering)
        self.rt.dominant, rtMaxValue  = getRT(self, self.rt)

        #Accident risk estimation
        poisson(self, self.speed.dominant, self.steering.dominant, self.rt.dominant, speedMaxValue, steeringMaxValue, rtMaxValue, self.distraction)

        #Update distraction value
        self.distraction = choice((0, 1), 1, (0.5, 0.5))
        
        pass


