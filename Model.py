from mesa import Model, Agent
from mesa.time import RandomActivation
from Agent import * 
from InputValues import *


class DrivingModel(Model):

    def __init__(self, N):
        self.num_drivers = N
        self.schedule = RandomActivation(self)
        #Create the drivers (agents)
        for i in range(self.num_drivers):
            driver_agent = DriverAgent(i, self, emotionValues,personalityValues, stressValue, distractionValue)
            self.schedule.add(driver_agent)
            
    def step(self):
        #Advance the model by one step.
        self.schedule.step()
    