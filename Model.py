from mesa import Model, Agent
from mesa.time import RandomActivation
from Agent import * 
from DriverCollector import DriverCollector 
import configparser
from numpy.random import choice




class DrivingModel(Model):

    def __init__(self, N):
        self.num_drivers = N
        self.schedule = RandomActivation(self)
        #Create the drivers (agents)
        for i in range(self.num_drivers):
            emotion = self.emotion_choice()
            emotionValues = self.load_emotions(emotion)
            personality = self.personality_choice()
            personalityValues = self.load_personality(personality)
            stress = self.stress_choice()
            stressValue = self.load_stress(stress)
            driver_agent = DriverAgent(i, self, emotionValues,personalityValues, stressValue)
            self.schedule.add(driver_agent)
        self.add_collectors()

    def add_collectors(self):
        self.driver_collector = DriverCollector(agent_reporters={"Emotions" : lambda a: a.emotions, "Personality" : lambda a: a.personality, "Stress" : lambda a: a.stress, "Speed" : lambda a: a.speed.dominant, "Acceleration" : lambda a: a.acceleration.dominant, "Braking" : lambda a: a.braking.dominant, "Steering" : lambda a: a.steering.dominant, "Response Time" : lambda a: a.rt.dominant })


    def load_emotions(self, emotion):
        config = configparser.ConfigParser()
        config.read('general.ini')
        emotionValues = dict(config[emotion])
        return emotionValues

    def load_personality(self, personality):
        config = configparser.ConfigParser()
        config.read('general.ini')
        personalityValues = dict(config[personality])
        return personalityValues

    def load_stress(self, stress):
        config = configparser.ConfigParser()
        config.read('general.ini')
        stressValue = str(config[stress]["Stress"])
        return stressValue

    def emotion_choice(self):
        emotion = choice(("HAPPINESS", "FEAR", "ANGER", "ANXIETY"), 1, (0.25,0.25, 0.25, 0.25))
        return emotion[0]

    def personality_choice(self):
        personality = choice(("RECKLESS DRIVER", "ANXIOUS DRIVER", "ANGRY DRIVER", "CAREFUL DRIVER"), 1, (0.25,0.25, 0.25, 0.25))
        return personality[0]
    
    def stress_choice(self):
        stress = choice(("ANXIOUS STRESS", "ANGRY STRESS", "NO STRESS"), 1, (1/3,1/3,1/3))
        return stress[0]


    def step(self):
        #Advance the model by one step.
        self.schedule.step()
        self.driver_collector.collect(self)
    