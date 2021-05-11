from mesa import Agent, Model 
from DrivingStyles import selectDrivingStyle

class DriverAgent(Agent):

    #Initializes DriverAgent object 
    def __init__(self, unique_id, model, stressValue, emotionValues, personalityValues, distractionValue):
        super().__init__(unique_id, model)
        #An agent is characterized by stress, emotions, personality traits and distraction
        #Stress, emotions and distraction can vary on each agent's step but personality traits remain constant 
        #Stress
        self.stress = stressValue
        #Emotions
        self.emotions = self.getEmotions(emotionValues)
        #Personality 
        self.personality = self.getPersonality(personalityValues)
        #Distraction
        self.distraction = distractionValue
        
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
        selectDrivingStyle(self, self.emotions, self.personality, self.stress)
        #getAccidentProbability(self)
        #updateInputs(self)
        pass
