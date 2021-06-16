#This script includes the main traits that characterize driving behaviour 

#Speed 
class Speed():
    def __init__(self):
        self.slow = 0
        self.appropiate = 0
        self.fast = 0

#Intensity and suddenness when accelerating 
class Acceleration():
    def __init__(self):
        self.slow = 0
        self.appropiate = 0
        self.fast = 0

#Intensity and suddenness when braking 
class Braking():
    def __init__(self):
        self.gentle = 0
        self.abrupt = 0

#Movement of the vehicle's wheel 
class SteeringWheel():
    def __init__(self):
        self.low = 0
        self.high = 0

#Response time in stress-related situations on the road
class ResponseTime():
    def __init__(self):
        self.low = 0
        self.high = 0

