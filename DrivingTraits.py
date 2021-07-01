#This script includes the main traits that characterize driving behaviour 

#Speed 
class Speed():
    def __init__(self):
        self.slow = 0
        self.appropriate = 0
        self.fast = 0
        self.dominant = ""


#Intensity and suddenness when accelerating 
class Acceleration():
    def __init__(self):
        self.slow = 0
        self.appropriate = 0
        self.fast = 0
        self.dominant = ""

#Intensity and suddenness when braking 
class Braking():
    def __init__(self):
        self.gentle = 0
        self.abrupt = 0
        self.dominant = ""


#Movement of the vehicle's wheel 
class SteeringWheel():
    def __init__(self):
        self.low = 0
        self.high = 0
        self.dominant = ""

#Response time in stress-related situations on the road
class ResponseTime():
    def __init__(self):
        self.low = 0
        self.high = 0
        self.dominant = ""

