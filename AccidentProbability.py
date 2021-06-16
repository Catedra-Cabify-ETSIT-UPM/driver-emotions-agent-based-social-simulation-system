import csv

def adaptMean():
    #3 hour drive
    drivingTime = 3
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
    print(total_accidents)
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
    print(index)
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
        print(counter)
    total_justified_accidents = total_accidents - counter
    print(total_justified_accidents)
    return total_justified_accidents

def getSpeedFrequency():
    speed_counter = 0
    adapter = adaptMean()
    #total_justified_accidents = getTotalJustifiedAccidents()
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
    print(speed_counter)
    #speed_accProbability = speed_counter/total_justified_accidents
    speed_rate = speed_counter*adapter
    print(speed_rate)
    return speed_rate

def getSteeringFrequency():
    steering_counter = 0
    adapter = adaptMean()
    #total_justified_accidents = getTotalJustifiedAccidents()
    steering_search1 = 'made an improper turn'
    steering_search2 = 'failure to keep in proper lane or running off road'
    steering_search3 = 'over-correcting/over-steering'
    steering_search4 = 'unsafe lane change'
    with open('data/Traffic_Crashes.csv', encoding='UTF-8') as f:
        csvreader = csv.reader(f)
        for line in csvreader:
            if any(steering_search1 in l for l in map(str.lower, line)) or any(steering_search2 in l for l in map(str.lower, line)) or any(steering_search3 in l for l in map(str.lower, line)) or any(steering_search4 in l for l in map(str.lower, line)):
                steering_counter += 1
    print(steering_counter)
    #steering_accProbability = steering_counter/total_justified_accidents
    steering_rate = steering_counter*adapter
    print(steering_rate)
    return steering_rate

def getRTFrequency():
    RT_counter = 0
    adapter = adaptMean()
    #total_justified_accidents = getTotalJustifiedAccidents()
    RT_search1 = 'followed too closely'
    RT_search2 = 'operating vehicle in erratic, reckless, careless, negligent or  aggressive manner'
    #RT_search3 = ''
    with open('data/Traffic_Crashes.csv', encoding='UTF-8') as f:
        csvreader = csv.reader(f)
        for line in csvreader:
            if any(RT_search1 in l for l in map(str.lower, line)) or any(RT_search2 in l for l in map(str.lower, line)):
                RT_counter += 1
    print(RT_counter)
    #RT_accProbability = RT_counter/total_justified_accidents
    RT_rate = RT_counter*adapter
    print(RT_rate)
    return RT_rate


def getExternalFactorsIndex():
    index = 0
    with open('data/Traffic_Crashes.csv', encoding='UTF-8') as f:
        csvreader = csv.reader(f)
        fields = next(csvreader)
        print(fields)
        for i in fields:
            if i == 'V1_Driver1':
                index = fields.index(i)
    print(index)
    return index

def getExtFactorsFrequency():
    #total_justified_accidents = getTotalJustifiedAccidents()
    index = getExternalFactorsIndex()
    exf_counter = 0
    adapter = adaptMean()
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
        print(exf_counter)
    #exf_accProbability = exf_counter/total_justified_accidents
    exf_rate = exf_counter*adapter
    print(exf_rate)
    return exf_rate

#getTotalAccidents()
#getVehicleIndex()
#getTotalJustifiedAccidents()
#getSpeedFrequency()
#getSteeringFrequency()
#getRTFrequency()
#getExtFactorsFrequency()
