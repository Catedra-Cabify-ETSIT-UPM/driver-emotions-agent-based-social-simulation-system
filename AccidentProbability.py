import csv
import configparser
import math

def adaptMean():
    #Driving time
    config = configparser.ConfigParser()
    config.read('general.ini')
    drivingTime = int(config["DRIVING TIME"]["time"])
    #4 year dataset
    totalHours = 4*365*24
    #Multiplier 
    mult = drivingTime/totalHours
    return mult

def getTotalAccidents():
    total_accidents = 0
    with open('data/Traffic_Crashes.csv', encoding='UTF-8') as f:
        csvreader = csv.reader(f)
        total_accidents = len(list(csvreader)) - 1
    #print(total_accidents)
    return total_accidents

def getVehicleIndex():
    index = 0
    with open('data/Traffic_Crashes.csv', encoding='UTF-8') as f:
        csvreader = csv.reader(f)
        fields = next(csvreader)
        print(fields)
        for i in fields:
            if i == 'V1_Vehicle':
                index = fields.index(i)
    #print(index)
    return index

def getTotalJustifiedAccidents():
    total_accidents = getTotalAccidents()
    total_justified_accidents = 0
    index = getVehicleIndex()
    counter = 0
    unknown_search = 'UNKNOWN'
    unregistered_search = ''
    with open('data/Traffic_Crashes.csv', encoding='UTF-8') as f:
        csvreader = csv.reader(f)
        for line in csvreader:
            if line[index] == unregistered_search:
                counter += 1
            elif line[index] == unknown_search:
                counter += 1
        #print(counter)
    total_justified_accidents = total_accidents - counter
    #print(total_justified_accidents)
    return total_justified_accidents

def getSpeedFrequency():
    speed_counter = 0
    speed_search1 = 'driving too fast for conditions'
    speed_search2 = 'exceeded authorized speed limit'
    speed_search3 = 'operating vehicle in erratic, reckless, careless, negligent or  aggressive manner'
    speed_search4 = 'failure to keep in proper lane or running off road'
    speed_search5 = 'unsafe lane change'
    with open('data/Traffic_Crashes.csv', encoding='UTF-8') as f:
        csvreader = csv.reader(f)
        for line in csvreader:
            if any(speed_search1 in l for l in map(str.lower, line)) or any(speed_search2 in l for l in map(str.lower, line)) or any(speed_search3 in l for l in map(str.lower, line)) or any(speed_search4 in l for l in map(str.lower, line)) or any(speed_search5 in l for l in map(str.lower, line)):
                speed_counter += 1
    #print(speed_counter)
    #speed_accProbability = speed_counter/total_justified_accidents
    return speed_counter

def getSteeringFrequency():
    steering_counter = 0
    steering_search1 = 'made an improper turn'
    steering_search2 = 'failure to keep in proper lane or running off road'
    steering_search3 = 'over-correcting/over-steering'
    steering_search4 = 'unsafe lane change'
    with open('data/Traffic_Crashes.csv', encoding='UTF-8') as f:
        csvreader = csv.reader(f)
        for line in csvreader:
            if any(steering_search1 in l for l in map(str.lower, line)) or any(steering_search2 in l for l in map(str.lower, line)) or any(steering_search3 in l for l in map(str.lower, line)) or any(steering_search4 in l for l in map(str.lower, line)):
                steering_counter += 1
    #print(steering_counter)
    #steering_accProbability = steering_counter/total_justified_accidents
    return steering_counter

def getRTFrequency():
    RT_counter = 0
    RT_search1 = 'followed too closely'
    RT_search2 = 'operating vehicle in erratic, reckless, careless, negligent or  aggressive manner'
    with open('data/Traffic_Crashes.csv', encoding='UTF-8') as f:
        csvreader = csv.reader(f)
        for line in csvreader:
            if any(RT_search1 in l for l in map(str.lower, line)) or any(RT_search2 in l for l in map(str.lower, line)):
                RT_counter += 1
    #print(RT_counter)
    #RT_accProbability = RT_counter/total_justified_accidents
    return RT_counter

def getExternalFactorsIndex():
    index = 0
    with open('data/Traffic_Crashes.csv', encoding='UTF-8') as f:
        csvreader = csv.reader(f)
        fields = next(csvreader)
        #print(fields)
        for i in fields:
            if i == 'V1_Driver1':
                index = fields.index(i)
   #print(index)
    return index

def getExtFactorsFrequency():
    index = getExternalFactorsIndex()
    exf_counter = 0
    distraction_search = 'INATTENTION/DISTRACTED'
    drinking_search = 'HAD BEEN DRINKING'
    drugs_search = 'DRUG INVOLVEMENT'
    with open('data/Traffic_Crashes.csv', encoding='UTF-8') as f:
        csvreader = csv.reader(f)
        for line in csvreader:
            if line[index] == distraction_search:
                exf_counter += 1
            elif line[index] == drinking_search:
                exf_counter += 1
            elif line[index] == drugs_search:
                exf_counter += 1
        #print(exf_counter)
    #exf_accProbability = exf_counter/total_justified_accidents
    return exf_counter

def definePoisson(occurrences, frequency):
    k = occurrences
    lambdaP = frequency*adaptMean()
    poissonProbability = ((lambdaP**k)*(math.e**-lambdaP))/(math.factorial(k))
    return poissonProbability

def poisson(self, speedMaxLevel, steeringMaxLevel, rtMaxLevel, speedMaxValue, steeringMaxValue, rtMaxValue, distraction):
    speedFrequency = getSpeedFrequency()
    steeringFrequency = getSteeringFrequency()
    rtFrequency = getRTFrequency()
    distractionFrequency = getExtFactorsFrequency()
    speedProb = 0
    steeringProb = 0
    rtProb = 0

    if distraction == 0:
        if speedMaxLevel == '[\'FAST\']':
            speedProb = definePoisson(1, speedFrequency)
        if steeringMaxLevel == '[\'HIGH\']':
            steeringProb = definePoisson(1, steeringFrequency)
        if rtMaxLevel == '[\'HIGH\']':
            rtProb = definePoisson(1, rtFrequency)
        
        if (speedProb > 0) and (speedMaxValue >= steeringMaxValue) and (speedMaxValue >= rtMaxValue):
            self.accidentProbability = speedProb
            return
        elif (steeringProb > 0) and (steeringMaxValue > speedMaxValue) and (steeringMaxValue > rtMaxValue):
            self.accidentProbability = steeringProb
            return 
        elif (rtProb > 0) and (rtMaxValue > speedMaxValue) and (rtMaxValue > steeringMaxValue):
            self.accidentProbability = steeringProb
            return 
        else:
            self.accidentProbability = 0.05
            return

    elif distraction == 1:
        distractionProb = definePoisson(1, distractionFrequency)
        if speedMaxLevel == '[\'FAST\']':
            speedProb = definePoisson(1, speedFrequency + distractionFrequency)
        if steeringMaxLevel == '[\'HIGH\']':
            steeringProb = definePoisson(1, steeringFrequency + distractionFrequency)
        if rtMaxLevel == '[\'HIGH\']':
            rtProb = definePoisson(1, rtFrequency + distractionFrequency)
        
        if (speedProb > 0) and (speedMaxValue >= steeringMaxValue) and (speedMaxValue >= rtMaxValue):
            self.accidentProbability = speedProb
            return
        elif (steeringProb > 0) and (steeringMaxValue > speedMaxValue) and (steeringMaxValue > rtMaxValue):
            self.accidentProbability = steeringProb
            return 
        elif (rtProb > 0) and (rtMaxValue > speedMaxValue) and (rtMaxValue > steeringMaxValue):
            self.accidentProbability = rtProb
            return 
        else:
            self.accidentProbability = 0.05 + distractionProb
            return
    
    else: 
        self.accidentProbability = 0.05
        return



#getTotalAccidents()
#getVehicleIndex()
#getTotalJustifiedAccidents()
# getSpeedFrequency()
# getSteeringFrequency()
# getRTFrequency()
# getExtFactorsFrequency()
