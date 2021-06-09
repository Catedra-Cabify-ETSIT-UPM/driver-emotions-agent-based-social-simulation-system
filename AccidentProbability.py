import csv

def getTotalAccidents():
    total_accidents = 0
    with open('data/traffic-crashes.csv', encoding='UTF-8') as f:
        csvreader = csv.reader(f)
        total_accidents = len(list(csvreader)) - 1
    print(total_accidents)
    return total_accidents

def getFieldIndex():
    index = 0
    with open('data/traffic-crashes.csv', encoding='UTF-8') as f:
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
    index = getFieldIndex()
    counter = 0
    unknown_search = 'UNKNOWN'
    unregistered_search = ''
    with open('data/traffic-crashes.csv', encoding='UTF-8') as f:
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

def getSpeedProbability():
    speed_counter = 0
    total_justified_accidents = getTotalJustifiedAccidents()
    speed_search1 = 'driving too fast for conditions'
    speed_search2 = 'exceeded authorized speed limit'
    speed_search3 = 'operating vehicle in erratic, reckless, careless, negligent or  aggressive manner'
    speed_search4 = 'failure to keep in proper lane or running off road'
    speed_search5 = 'unsafe lane change'
    with open('data/traffic-crashes.csv', encoding='UTF-8') as f:
        csvreader = csv.reader(f)
        for line in csvreader:
            if any(speed_search1 in l for l in map(str.lower, line)) or any(speed_search2 in l for l in map(str.lower, line)) or any(speed_search3 in l for l in map(str.lower, line)) or any(speed_search4 in l for l in map(str.lower, line)) or any(speed_search5 in l for l in map(str.lower, line)):
                speed_counter += 1
    print(speed_counter)
    speed_accProbability = speed_counter/total_justified_accidents
    print(speed_accProbability)
    return speed_accProbability

def getSteeringProbability():
    steering_counter = 0
    total_justified_accidents = getTotalJustifiedAccidents()
    steering_search1 = 'made an improper turn'
    steering_search2 = 'failure to keep in proper lane or running off road'
    steering_search3 = 'over-correcting/over-steering'
    steering_search4 = 'unsafe lane change'
    with open('data/traffic-crashes.csv', encoding='UTF-8') as f:
        csvreader = csv.reader(f)
        for line in csvreader:
            if any(steering_search1 in l for l in map(str.lower, line)) or any(steering_search2 in l for l in map(str.lower, line)) or any(steering_search3 in l for l in map(str.lower, line)) or any(steering_search4 in l for l in map(str.lower, line)):
                steering_counter += 1
    print(steering_counter)
    steering_accProbability = steering_counter/total_justified_accidents
    print(steering_accProbability)
    return steering_accProbability

def getRTProbability():
    RT_counter = 0
    total_justified_accidents = getTotalJustifiedAccidents()
    RT_search1 = 'followed too closely'
    RT_search2 = 'operating vehicle in erratic, reckless, careless, negligent or  aggressive manner'
    #RT_search3 = ''
    with open('data/traffic-crashes.csv', encoding='UTF-8') as f:
        csvreader = csv.reader(f)
        for line in csvreader:
            if any(RT_search1 in l for l in map(str.lower, line)) or any(RT_search2 in l for l in map(str.lower, line)):
                RT_counter += 1
    print(RT_counter)
    RT_accProbability = RT_counter/total_justified_accidents
    print(RT_accProbability)
    return RT_accProbability


def getDistractionProbability():
    

#getTotalAccidents()
#getFieldIndex()
#getTotalJustifiedAccidents()
#getSpeedProbability()
#getSteeringProbability()
#getRTProbability()