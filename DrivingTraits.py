#This script includes the main traits that characterize driving behaviour 

from enum import Enum

#Speed 
class Speed(Enum):
    SLOW = 0
    APPROPIATE = 0
    FAST = 0

#Intensity and suddenness when accelerating 
class Acceleration(Enum):
    SLOW = 0
    APPROPIATE = 0
    FAST = 0

#Intensity and suddenness when braking 
class Braking(Enum):
    GENTLE = 0
    ABRUPT = 0

#Movement of the vehicle's wheel 
class SteeringWheel(Enum):
    LOW = 0
    HIGH = 0

#Response time in stress-related situations on the road
class ResponseTime(Enum):
    LOW = 0
    HIGH = 0

