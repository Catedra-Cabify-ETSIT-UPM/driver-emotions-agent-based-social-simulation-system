from DrivingTraits import *
from Emotions import evaluateEmotions
from Personality import evaluatePersonality
#from random import choice


def init_ds(self):
    global reckless_ds
    reckless_ds = 0
    global angry_ds 
    angry_ds = 0
    global anxious_ds 
    anxious_ds = 0
    global careful_ds
    careful_ds = 0

#Emotions contribution to the driving style
def emotionsDrivingStyle(self, emotions):
    self.evaluateEmotions(emotions)
    #Check reckless driving style 
    if ((Speed.SLOW == 1 or Speed.FAST == 1) and (Acceleration.SLOW == 1 or Acceleration.FAST == 1) and Braking.ABRUPT == 1 and SteeringWheel.HIGH == 1 and (ResponseTime.LOW == 1 or ResponseTime.HIGH == 1)):
        reckless_ds=+1
    
    #Check anxious driving style:
    elif (Speed.FAST == 1 and Acceleration.FAST == 1 and Braking.ABRUPT == 1 and SteeringWheel.HIGH == 1 and ResponseTime.HIGH == 1):
        anxious_ds=+1

    #Check angry driving style:
    elif (Speed.FAST == 1 and Acceleration.FAST == 1 and Braking.ABRUPT == 1 and SteeringWheel.HIGH == 1 and ResponseTime.LOW == 1):
        angry_ds=+1

    #Check careful driving style:
    elif (Speed.APPROPIATE == 1 and Acceleration.APPROPIATE == 1 and Braking.GENTLE == 1 and SteeringWheel.LOW == 1 and ResponseTime.LOW == 1):
        careful_ds=+1
 
 #Personality contribution to the driving style
def personalityDrivingStyle(self, personality):
    drivingStyle = self.evaluatePersonality(personality)
    if drivingStyle == "RECKLESS":
        reckless_ds=+1
    elif drivingStyle == "ANXIOUS":
        anxious_ds=+1
    elif drivingStyle == "ANGRY":
        angry_ds=+1
    elif drivingStyle == "CAREFUL":
        careful_ds=+1
    else:
        return

#Stress contribution to the driving style
def stressDrivingStyle(self, stress):
    if stress == 1:
        #Contribution to both anxious and angry driving styles
        anxious_ds=+1
        angry_ds=+1
        #Contribution to either anxious or angry driving styles
        #stressOutcome = random.choice(["AnxiousDriving", "AngryDriving"])
        #if stressOutcome == "AnxiousDriving":
            #anxious_ds =+1
            #print("Stress caused an ANXIOUS driving style")
        #else:
            #angry_ds =+1
            #print("Stress caused an ANGRY driving style")
    else: 
        print("There is not stress contribution")

#Choose dominant driving style
def selectDrivingStyle(self, emotions, personality, stress):
    self.init_ds()
    self.emotionsDrivingStyle(emotions)
    self.personalityDrivingStyle(personality)
    self.stressDrivingStyle(stress)
