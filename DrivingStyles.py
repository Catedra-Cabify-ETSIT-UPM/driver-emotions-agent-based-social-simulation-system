from DrivingTraits import *
from Emotions import evaluateEmotions
from Personality import evaluatePersonality
from Stress import evaluateStress
#from random import choice

def biggest(a, b, c):
    # Define a dictionary d with strings 'a','b','c' as keys to associate with values
    d = {'a': a, 'b': b, 'c': c}
    # Find the maximum value
    maxValue = max(d.values())
    # Gather all keys corresponding to max value into list
    maxLetters = [k for k,v in d.items() if v == maxValue]
    return maxLetters, maxValue

def getSpeed(self, speed):
    values = {"SLOW": self.speed.slow, "APPROPIATE": self.speed.appropiate, "FAST": self.speed.fast}
    maxValue = max(values.values())
    maxLevel = [k for k,v in values.items() if v == maxValue]
    return maxLevel, maxValue

def getAcceleration(self, acceleration):
    values = {"SLOW": self.acceleration.slow, "APPROPIATE": self.acceleration.appropiate, "FAST": self.acceleration.fast}
    maxValue = max(values.values())
    maxLevel = [k for k,v in values.items() if v == maxValue]
    return maxLevel, maxValue

def getBraking(self, braking):
    values = {"GENTLE": self.braking.gentle, "ABRUPT": self.braking.appropiate}
    maxValue = max(values.values())
    maxLevel = [k for k,v in values.items() if v == maxValue]
    return maxLevel, maxValue

def getSteering(self, steering):
    values = {"LOW": self.steering.low, "HIGH": self.steering.high}
    maxValue = max(values.values())
    maxLevel = [k for k,v in values.items() if v == maxValue]
    return maxLevel, maxValue

def getRT(self, rt):
    values = {"LOW": self.rt.low, "HIGH": self.rt.high}
    maxValue = max(values.values())
    maxLevel = [k for k,v in values.items() if v == maxValue]
    return maxLevel, maxValue

def setDrivingStyle(self, speed, acceleration, braking, steering, rt):
    drivingStyle = {}
    [speedLevel, speedValue] = getSpeed(self, speed)
    drivingStyle ["Speed " + speedLevel] = speedValue
    [accelerationLevel, accelerationValue] = getAcceleration(self, acceleration)
    drivingStyle ["Acceleration " + accelerationLevel] = accelerationValue
    [brakingLevel, brakingValue] = getBraking(self, braking)
    drivingStyle ["Braking " + brakingLevel] = brakingValue
    [steeringLevel, steeringValue] = getSteering(self, steering)
    drivingStyle ["Steering " + steeringLevel] = steeringValue
    [rtLevel, rtValue] = getRT(self, rt)
    drivingStyle ["RT " + rtLevel] = rtValue
    return drivingStyle

