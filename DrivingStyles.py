from DrivingTraits import *
from Emotions import evaluateEmotions
from Personality import evaluatePersonality
from Stress import evaluateStress

def getSpeed(self, speed):
    values = {"SLOW": self.speed.slow, "APPROPRIATE": self.speed.appropriate, "FAST": self.speed.fast}
    maxValue = max(values.values())
    maxLevel = str([k for k,v in values.items() if v == maxValue])
    return maxLevel, maxValue

def getAcceleration(self, acceleration):
    values = {"SLOW": self.acceleration.slow, "APPROPRIATE": self.acceleration.appropriate, "FAST": self.acceleration.fast}
    maxValue = max(values.values())
    maxLevel = str([k for k,v in values.items() if v == maxValue])
    return maxLevel, maxValue

def getBraking(self, braking):
    values = {"GENTLE": self.braking.gentle, "ABRUPT": self.braking.abrupt}
    maxValue = max(values.values())
    maxLevel = str([k for k,v in values.items() if v == maxValue])
    return maxLevel, maxValue

def getSteering(self, steering):
    values = {"LOW": self.steering.low, "HIGH": self.steering.high}
    maxValue = max(values.values())
    maxLevel = str([k for k,v in values.items() if v == maxValue])
    return maxLevel, maxValue

def getRT(self, rt):
    values = {"LOW": self.rt.low, "HIGH": self.rt.high}
    maxValue = max(values.values())
    maxLevel = str([k for k,v in values.items() if v == maxValue])
    return maxLevel, maxValue



