from mesa import Agent, Model 
from DrivingTraits import *
from Emotions import evaluateEmotions
from Personality import evaluatePersonality
from Stress import evaluateStress
from DrivingStyles import setDrivingStyle
from AccidentProbability import *

class DriverAgent(Agent):

    #Initializes DriverAgent object 
    def __init__(self, unique_id, model, emotionValues, personalityValues, stressValue, distractionValue):
        super().__init__(unique_id, model)
        #An agent is characterized by emotions, personality traits and stress
        #Stress, emotions can vary on each agent's step but personality traits remain constant 
        #Emotions
        self.emotions = self.getEmotions(emotionValues)
        #Personality 
        self.personality = self.getPersonality(personalityValues)
        #Stress
        self.stress = stressValue
        #Distraction
        self.distraction = distractionValue
        #Driving traits
        self.speed = Speed()
        self.acceleration = Acceleration()
        self.braking = Braking()
        self.steering = SteeringWheel()
        self.rt = ResponseTime()
        #Accident rate
        self.accidentRate = 0
        
    def getEmotions(self, emotionValues):
        emotion_names = ["Happyness", "Fear", "Anger", "Anxiety"]
        emotions = zip(emotion_names, emotionValues)
        return emotions

    def getPersonality(self, personalityValues):
        personality_names = ["Extraversion", "Agreeableness", "Conscientiousness", "Neuroticism", "Openness"]
        personality = zip(personality_names, personalityValues)
        return personality  
    
    def step(self):
        #The agent's step is defined here.
        evaluateEmotions(self, self.emotions)
        evaluatePersonality(self, self.personality)
        evaluateStress(self, self.stress)
        drivingStyle = setDrivingStyle(self, self.speed, self.acceleration, self.braking, self.steering, self.rt)
        if ("Speed FAST" in drivingStyle) or ("Acceleration FAST" in drivingStyle):
            self.accidentRate = getSpeedFrequency() 
        elif "Steering HIGH" in drivingStyle:
            self.accidentRate = getSteeringFrequency()
        elif "RT HIGH" in drivingStyle:
            self.accidentRate = getRTFrequency()
        else: 
            pass
        #VARIABILITY
        pass


