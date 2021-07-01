import pandas as pd
import numpy as np
import math

def happinessSpeed():
    counter1 = 0
    counter2 = 0
    counter3 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Emotions == '{\'happiness\': \'1\', \'fear\': \'0\', \'anger\': \'0\', \'anxiety\': \'0\'}']
    boolFiltered = filtered['Speed'].str.contains('SLOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Speed'].str.contains('APPROPRIATE')
    counter2 = boolFiltered.sum()
    boolFiltered = filtered['Speed'].str.contains('FAST')
    counter3 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    print(counter3)
    return counter1, counter2, counter3

def fearSpeed():
    counter1 = 0
    counter2 = 0
    counter3 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Emotions == '{\'happiness\': \'0\', \'fear\': \'1\', \'anger\': \'0\', \'anxiety\': \'0\'}']
    boolFiltered = filtered['Speed'].str.contains('SLOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Speed'].str.contains('APPROPRIATE')
    counter2 = boolFiltered.sum()
    boolFiltered = filtered['Speed'].str.contains('FAST')
    counter3 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    print(counter3)
    return counter1, counter2, counter3

def angerSpeed():
    counter1 = 0
    counter2 = 0
    counter3 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Emotions == '{\'happiness\': \'0\', \'fear\': \'0\', \'anger\': \'1\', \'anxiety\': \'0\'}']
    boolFiltered = filtered['Speed'].str.contains('SLOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Speed'].str.contains('APPROPRIATE')
    counter2 = boolFiltered.sum()
    boolFiltered = filtered['Speed'].str.contains('FAST')
    counter3 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    print(counter3)
    return counter1, counter2, counter3

def anxietySpeed():
    counter1 = 0
    counter2 = 0
    counter3 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Emotions == '{\'happiness\': \'0\', \'fear\': \'0\', \'anger\': \'0\', \'anxiety\': \'1\'}']
    boolFiltered = filtered['Speed'].str.contains('SLOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Speed'].str.contains('APPROPRIATE')
    counter2 = boolFiltered.sum()
    boolFiltered = filtered['Speed'].str.contains('FAST')
    counter3 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    print(counter3)
    return counter1, counter2, counter3

# happinessSpeed()
# fearSpeed()
# angerSpeed()
# anxietySpeed()


def happinessAcceleration():
    counter1 = 0
    counter2 = 0
    counter3 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Emotions == '{\'happiness\': \'1\', \'fear\': \'0\', \'anger\': \'0\', \'anxiety\': \'0\'}']
    boolFiltered = filtered['Acceleration'].str.contains('SLOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Acceleration'].str.contains('APPROPRIATE')
    counter2 = boolFiltered.sum()
    boolFiltered = filtered['Acceleration'].str.contains('FAST')
    counter3 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    print(counter3)
    return counter1, counter2, counter3

def fearAcceleration():
    counter1 = 0
    counter2 = 0
    counter3 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Emotions == '{\'happiness\': \'0\', \'fear\': \'1\', \'anger\': \'0\', \'anxiety\': \'0\'}']
    boolFiltered = filtered['Acceleration'].str.contains('SLOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Acceleration'].str.contains('APPROPRIATE')
    counter2 = boolFiltered.sum()
    boolFiltered = filtered['Acceleration'].str.contains('FAST')
    counter3 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    print(counter3)
    return counter1, counter2, counter3

def angerAcceleration():
    counter1 = 0
    counter2 = 0
    counter3 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Emotions == '{\'happiness\': \'0\', \'fear\': \'0\', \'anger\': \'1\', \'anxiety\': \'0\'}']
    boolFiltered = filtered['Acceleration'].str.contains('SLOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Acceleration'].str.contains('APPROPRIATE')
    counter2 = boolFiltered.sum()
    boolFiltered = filtered['Acceleration'].str.contains('FAST')
    counter3 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    print(counter3)
    return counter1, counter2, counter3

def anxietyAcceleration():
    counter1 = 0
    counter2 = 0
    counter3 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Emotions == '{\'happiness\': \'0\', \'fear\': \'0\', \'anger\': \'0\', \'anxiety\': \'1\'}']
    boolFiltered = filtered['Acceleration'].str.contains('SLOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Acceleration'].str.contains('APPROPRIATE')
    counter2 = boolFiltered.sum()
    boolFiltered = filtered['Acceleration'].str.contains('FAST')
    counter3 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    print(counter3)
    return counter1, counter2, counter3


# happinessAcceleration()
# fearAcceleration()
# angerAcceleration()
# anxietyAcceleration()


def happinessBraking():
    counter1 = 0
    counter2 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Emotions == '{\'happiness\': \'1\', \'fear\': \'0\', \'anger\': \'0\', \'anxiety\': \'0\'}']
    boolFiltered = filtered['Braking'].str.contains('GENTLE')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Braking'].str.contains('ABRUPT')
    counter2 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    return counter1, counter2

def fearBraking():
    counter1 = 0
    counter2 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Emotions == '{\'happiness\': \'0\', \'fear\': \'1\', \'anger\': \'0\', \'anxiety\': \'0\'}']
    boolFiltered = filtered['Braking'].str.contains('GENTLE')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Braking'].str.contains('ABRUPT')
    counter2 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    return counter1, counter2

def angerBraking():
    counter1 = 0
    counter2 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Emotions == '{\'happiness\': \'0\', \'fear\': \'0\', \'anger\': \'1\', \'anxiety\': \'0\'}']
    boolFiltered = filtered['Braking'].str.contains('GENTLE')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Braking'].str.contains('ABRUPT')
    counter2 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    return counter1, counter2

def anxietyBraking():
    counter1 = 0
    counter2 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Emotions == '{\'happiness\': \'0\', \'fear\': \'0\', \'anger\': \'0\', \'anxiety\': \'1\'}']
    boolFiltered = filtered['Braking'].str.contains('GENTLE')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Braking'].str.contains('ABRUPT')
    counter2 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    return counter1, counter2

# happinessBraking()
# fearBraking()
# angerBraking()
# anxietyBraking()


def happinessSteering():
    counter1 = 0
    counter2 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Emotions == '{\'happiness\': \'1\', \'fear\': \'0\', \'anger\': \'0\', \'anxiety\': \'0\'}']
    boolFiltered = filtered['Steering'].str.contains('LOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Steering'].str.contains('HIGH')
    counter2 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    return counter1, counter2

def fearSteering():
    counter1 = 0
    counter2 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Emotions == '{\'happiness\': \'0\', \'fear\': \'1\', \'anger\': \'0\', \'anxiety\': \'0\'}']
    boolFiltered = filtered['Steering'].str.contains('LOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Steering'].str.contains('HIGH')
    counter2 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    return counter1, counter2

def angerSteering():
    counter1 = 0
    counter2 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Emotions == '{\'happiness\': \'0\', \'fear\': \'0\', \'anger\': \'1\', \'anxiety\': \'0\'}']
    boolFiltered = filtered['Steering'].str.contains('LOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Steering'].str.contains('HIGH')
    counter2 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    return counter1, counter2

def anxietySteering():
    counter1 = 0
    counter2 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Emotions == '{\'happiness\': \'0\', \'fear\': \'0\', \'anger\': \'0\', \'anxiety\': \'1\'}']
    boolFiltered = filtered['Steering'].str.contains('LOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Steering'].str.contains('HIGH')
    counter2 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    return counter1, counter2

# happinessSteering()
# fearSteering()
# angerSteering()
# anxietySteering()

def happinessRT():
    counter1 = 0
    counter2 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Emotions == '{\'happiness\': \'1\', \'fear\': \'0\', \'anger\': \'0\', \'anxiety\': \'0\'}']
    boolFiltered = filtered['Response Time'].str.contains('LOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Response Time'].str.contains('HIGH')
    counter2 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    return counter1, counter2

def fearRT():
    counter1 = 0
    counter2 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Emotions == '{\'happiness\': \'0\', \'fear\': \'1\', \'anger\': \'0\', \'anxiety\': \'0\'}']
    boolFiltered = filtered['Response Time'].str.contains('LOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Response Time'].str.contains('HIGH')
    counter2 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    return counter1, counter2

def angerRT():
    counter1 = 0
    counter2 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Emotions == '{\'happiness\': \'0\', \'fear\': \'0\', \'anger\': \'1\', \'anxiety\': \'0\'}']
    boolFiltered = filtered['Response Time'].str.contains('LOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Response Time'].str.contains('HIGH')
    counter2 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    return counter1, counter2

def anxietyRT():
    counter1 = 0
    counter2 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Emotions == '{\'happiness\': \'0\', \'fear\': \'0\', \'anger\': \'0\', \'anxiety\': \'1\'}']
    boolFiltered = filtered['Response Time'].str.contains('LOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Response Time'].str.contains('HIGH')
    counter2 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    return counter1, counter2

# happinessRT()
# fearRT()
# angerRT()
# anxietyRT()



#-----------------------------------------------------------------------------------------------------------------------------------------

def recklessSpeed():
    counter1 = 0
    counter2 = 0
    counter3 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Personality == '{\'extraversion\': \'1\', \'agreeableness\': \'-1\', \'conscientiousness\': \'-1\', \'neuroticism\': \'1\', \'openness\': \'0\'}']
    boolFiltered = filtered['Speed'].str.contains('SLOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Speed'].str.contains('APPROPRIATE')
    counter2 = boolFiltered.sum()
    boolFiltered = filtered['Speed'].str.contains('FAST')
    counter3 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    print(counter3)
    return counter1, counter2, counter3

def anxiousSpeed():
    counter1 = 0
    counter2 = 0
    counter3 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Personality == '{\'extraversion\': \'0\', \'agreeableness\': \'-1\', \'conscientiousness\': \'-1\', \'neuroticism\': \'1\', \'openness\': \'1\'}']
    boolFiltered = filtered['Speed'].str.contains('SLOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Speed'].str.contains('APPROPRIATE')
    counter2 = boolFiltered.sum()
    boolFiltered = filtered['Speed'].str.contains('FAST')
    counter3 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    print(counter3)
    return counter1, counter2, counter3

def angrySpeed():
    counter1 = 0
    counter2 = 0
    counter3 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Personality == '{\'extraversion\': \'0\', \'agreeableness\': \'-1\', \'conscientiousness\': \'-1\', \'neuroticism\': \'1\', \'openness\': \'-1\'}']
    boolFiltered = filtered['Speed'].str.contains('SLOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Speed'].str.contains('APPROPRIATE')
    counter2 = boolFiltered.sum()
    boolFiltered = filtered['Speed'].str.contains('FAST')
    counter3 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    print(counter3)
    return counter1, counter2, counter3

def carefulSpeed():
    counter1 = 0
    counter2 = 0
    counter3 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Personality == '{\'extraversion\': \'1\', \'agreeableness\': \'1\', \'conscientiousness\': \'1\', \'neuroticism\': \'-1\', \'openness\': \'1\'}']
    boolFiltered = filtered['Speed'].str.contains('SLOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Speed'].str.contains('APPROPRIATE')
    counter2 = boolFiltered.sum()
    boolFiltered = filtered['Speed'].str.contains('FAST')
    counter3 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    print(counter3)
    return counter1, counter2, counter3

# recklessSpeed()
# anxiousSpeed()
# angrySpeed()
# carefulSpeed()


def recklessAcceleration():
    counter1 = 0
    counter2 = 0
    counter3 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Personality == '{\'extraversion\': \'1\', \'agreeableness\': \'-1\', \'conscientiousness\': \'-1\', \'neuroticism\': \'1\', \'openness\': \'0\'}']
    boolFiltered = filtered['Acceleration'].str.contains('SLOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Acceleration'].str.contains('APPROPRIATE')
    counter2 = boolFiltered.sum()
    boolFiltered = filtered['Acceleration'].str.contains('FAST')
    counter3 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    print(counter3)
    return counter1, counter2, counter3

def anxiousAcceleration():
    counter1 = 0
    counter2 = 0
    counter3 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Personality == '{\'extraversion\': \'0\', \'agreeableness\': \'-1\', \'conscientiousness\': \'-1\', \'neuroticism\': \'1\', \'openness\': \'1\'}']
    boolFiltered = filtered['Acceleration'].str.contains('SLOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Acceleration'].str.contains('APPROPRIATE')
    counter2 = boolFiltered.sum()
    boolFiltered = filtered['Acceleration'].str.contains('FAST')
    counter3 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    print(counter3)
    return counter1, counter2, counter3

def angryAcceleration():
    counter1 = 0
    counter2 = 0
    counter3 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Personality == '{\'extraversion\': \'0\', \'agreeableness\': \'-1\', \'conscientiousness\': \'-1\', \'neuroticism\': \'1\', \'openness\': \'-1\'}']
    boolFiltered = filtered['Acceleration'].str.contains('SLOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Acceleration'].str.contains('APPROPRIATE')
    counter2 = boolFiltered.sum()
    boolFiltered = filtered['Acceleration'].str.contains('FAST')
    counter3 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    print(counter3)
    return counter1, counter2, counter3

def carefulAcceleration():
    counter1 = 0
    counter2 = 0
    counter3 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Personality == '{\'extraversion\': \'1\', \'agreeableness\': \'1\', \'conscientiousness\': \'1\', \'neuroticism\': \'-1\', \'openness\': \'1\'}']
    boolFiltered = filtered['Acceleration'].str.contains('SLOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Acceleration'].str.contains('APPROPRIATE')
    counter2 = boolFiltered.sum()
    boolFiltered = filtered['Acceleration'].str.contains('FAST')
    counter3 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    print(counter3)
    return counter1, counter2, counter3

# recklessAcceleration()
# anxiousAcceleration()
# angryAcceleration()
# carefulAcceleration()

def recklessBraking():
    counter1 = 0
    counter2 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Personality == '{\'extraversion\': \'1\', \'agreeableness\': \'-1\', \'conscientiousness\': \'-1\', \'neuroticism\': \'1\', \'openness\': \'0\'}']
    boolFiltered = filtered['Braking'].str.contains('GENTLE')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Braking'].str.contains('ABRUPT')
    counter2 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    return counter1, counter2

def anxiousBraking():
    counter1 = 0
    counter2 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Personality == '{\'extraversion\': \'0\', \'agreeableness\': \'-1\', \'conscientiousness\': \'-1\', \'neuroticism\': \'1\', \'openness\': \'1\'}']
    boolFiltered = filtered['Braking'].str.contains('GENTLE')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Braking'].str.contains('ABRUPT')
    counter2 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    return counter1, counter2

def angryBraking():
    counter1 = 0
    counter2 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Personality == '{\'extraversion\': \'0\', \'agreeableness\': \'-1\', \'conscientiousness\': \'-1\', \'neuroticism\': \'1\', \'openness\': \'-1\'}']
    boolFiltered = filtered['Braking'].str.contains('GENTLE')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Braking'].str.contains('ABRUPT')
    counter2 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    return counter1, counter2

def carefulBraking():
    counter1 = 0
    counter2 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Personality == '{\'extraversion\': \'1\', \'agreeableness\': \'1\', \'conscientiousness\': \'1\', \'neuroticism\': \'-1\', \'openness\': \'1\'}']
    boolFiltered = filtered['Braking'].str.contains('GENTLE')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Braking'].str.contains('ABRUPT')
    counter2 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    return counter1, counter2

# recklessBraking()
# anxiousBraking()
# angryBraking()
# carefulBraking()

def recklessSteering():
    counter1 = 0
    counter2 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Personality == '{\'extraversion\': \'1\', \'agreeableness\': \'-1\', \'conscientiousness\': \'-1\', \'neuroticism\': \'1\', \'openness\': \'0\'}']
    boolFiltered = filtered['Steering'].str.contains('LOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Steering'].str.contains('HIGH')
    counter2 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    return counter1, counter2

def anxiousSteering():
    counter1 = 0
    counter2 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Personality == '{\'extraversion\': \'0\', \'agreeableness\': \'-1\', \'conscientiousness\': \'-1\', \'neuroticism\': \'1\', \'openness\': \'1\'}']
    boolFiltered = filtered['Steering'].str.contains('LOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Steering'].str.contains('HIGH')
    counter2 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    return counter1, counter2

def angrySteering():
    counter1 = 0
    counter2 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Personality == '{\'extraversion\': \'0\', \'agreeableness\': \'-1\', \'conscientiousness\': \'-1\', \'neuroticism\': \'1\', \'openness\': \'-1\'}']
    boolFiltered = filtered['Steering'].str.contains('LOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Steering'].str.contains('HIGH')
    counter2 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    return counter1, counter2

def carefulSteering():
    counter1 = 0
    counter2 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Personality == '{\'extraversion\': \'1\', \'agreeableness\': \'1\', \'conscientiousness\': \'1\', \'neuroticism\': \'-1\', \'openness\': \'1\'}']
    boolFiltered = filtered['Steering'].str.contains('LOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Steering'].str.contains('HIGH')
    counter2 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    return counter1, counter2

# recklessSteering()
# anxiousSteering()
# angrySteering()
# carefulSteering()

def recklessRT():
    counter1 = 0
    counter2 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Personality == '{\'extraversion\': \'1\', \'agreeableness\': \'-1\', \'conscientiousness\': \'-1\', \'neuroticism\': \'1\', \'openness\': \'0\'}']
    boolFiltered = filtered['Response Time'].str.contains('LOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Response Time'].str.contains('HIGH')
    counter2 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    return counter1, counter2

def anxiousRT():
    counter1 = 0
    counter2 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Personality == '{\'extraversion\': \'0\', \'agreeableness\': \'-1\', \'conscientiousness\': \'-1\', \'neuroticism\': \'1\', \'openness\': \'1\'}']
    boolFiltered = filtered['Response Time'].str.contains('LOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Response Time'].str.contains('HIGH')
    counter2 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    return counter1, counter2

def angryRT():
    counter1 = 0
    counter2 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Personality == '{\'extraversion\': \'0\', \'agreeableness\': \'-1\', \'conscientiousness\': \'-1\', \'neuroticism\': \'1\', \'openness\': \'-1\'}']
    boolFiltered = filtered['Response Time'].str.contains('LOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Response Time'].str.contains('HIGH')
    counter2 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    return counter1, counter2

def carefulRT():
    counter1 = 0
    counter2 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Personality == '{\'extraversion\': \'1\', \'agreeableness\': \'1\', \'conscientiousness\': \'1\', \'neuroticism\': \'-1\', \'openness\': \'1\'}']
    boolFiltered = filtered['Response Time'].str.contains('LOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Response Time'].str.contains('HIGH')
    counter2 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    return counter1, counter2

# recklessRT()
# anxiousRT()
# angryRT()
# carefulRT()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def angryStressSpeed():
    counter1 = 0
    counter2 = 0
    counter3 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Stress == 'Anger']
    boolFiltered = filtered['Speed'].str.contains('SLOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Speed'].str.contains('APPROPRIATE')
    counter2 = boolFiltered.sum()
    boolFiltered = filtered['Speed'].str.contains('FAST')
    counter3 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    print(counter3)
    return counter1, counter2, counter3

def anxiousStressSpeed():
    counter1 = 0
    counter2 = 0
    counter3 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Stress == 'Anxiety']
    boolFiltered = filtered['Speed'].str.contains('SLOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Speed'].str.contains('APPROPRIATE')
    counter2 = boolFiltered.sum()
    boolFiltered = filtered['Speed'].str.contains('FAST')
    counter3 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    print(counter3)
    return counter1, counter2, counter3

def noStressSpeed():
    counter1 = 0
    counter2 = 0
    counter3 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Stress.isnull()]
    boolFiltered = filtered['Speed'].str.contains('SLOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Speed'].str.contains('APPROPRIATE')
    counter2 = boolFiltered.sum()
    boolFiltered = filtered['Speed'].str.contains('FAST')
    counter3 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    print(counter3)
    return counter1, counter2, counter3



# angryStressSpeed()
# anxiousStressSpeed()
# noStressSpeed()

def angryStressAcceleration():
    counter1 = 0
    counter2 = 0
    counter3 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Stress == 'Anger']
    boolFiltered = filtered['Acceleration'].str.contains('SLOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Acceleration'].str.contains('APPROPRIATE')
    counter2 = boolFiltered.sum()
    boolFiltered = filtered['Acceleration'].str.contains('FAST')
    counter3 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    print(counter3)
    return counter1, counter2, counter3

def anxiousStressAcceleration():
    counter1 = 0
    counter2 = 0
    counter3 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Stress == 'Anxiety']
    boolFiltered = filtered['Acceleration'].str.contains('SLOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Acceleration'].str.contains('APPROPRIATE')
    counter2 = boolFiltered.sum()
    boolFiltered = filtered['Acceleration'].str.contains('FAST')
    counter3 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    print(counter3)
    return counter1, counter2, counter3

def noStressAcceleration():
    counter1 = 0
    counter2 = 0
    counter3 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Stress.isnull()]
    boolFiltered = filtered['Acceleration'].str.contains('SLOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Acceleration'].str.contains('APPROPRIATE')
    counter2 = boolFiltered.sum()
    boolFiltered = filtered['Acceleration'].str.contains('FAST')
    counter3 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    print(counter3)
    return counter1, counter2, counter3



# angryStressAcceleration()
# anxiousStressAcceleration()
# noStressAcceleration()


def angryStressBraking():
    counter1 = 0
    counter2 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Stress == 'Anger']
    boolFiltered = filtered['Braking'].str.contains('GENTLE')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Braking'].str.contains('ABRUPT')
    counter2 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    return counter1, counter2

def anxiousStressBraking():
    counter1 = 0
    counter2 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Stress == 'Anxiety']
    boolFiltered = filtered['Braking'].str.contains('GENTLE')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Braking'].str.contains('ABRUPT')
    counter2 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    return counter1, counter2

def noStressBraking():
    counter1 = 0
    counter2 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Stress.isnull()]
    boolFiltered = filtered['Braking'].str.contains('GENTLE')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Braking'].str.contains('ABRUPT')
    counter2 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    return counter1, counter2



# angryStressBraking()
# anxiousStressBraking()
# noStressBraking()

def angryStressSteering():
    counter1 = 0
    counter2 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Stress == 'Anger']
    boolFiltered = filtered['Steering'].str.contains('LOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Steering'].str.contains('HIGH')
    counter2 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    return counter1, counter2

def anxiousStressSteering():
    counter1 = 0
    counter2 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Stress == 'Anxiety']
    boolFiltered = filtered['Steering'].str.contains('LOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Steering'].str.contains('HIGH')
    counter2 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    return counter1, counter2

def noStressSteering():
    counter1 = 0
    counter2 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Stress.isnull()]
    boolFiltered = filtered['Steering'].str.contains('LOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Steering'].str.contains('HIGH')
    counter2 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    return counter1, counter2



# angryStressSteering()
# anxiousStressSteering()
# noStressSteering()

def angryStressRT():
    counter1 = 0
    counter2 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Stress == 'Anger']
    boolFiltered = filtered['Response Time'].str.contains('LOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Response Time'].str.contains('HIGH')
    counter2 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    return counter1, counter2

def anxiousStressRT():
    counter1 = 0
    counter2 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Stress == 'Anxiety']
    boolFiltered = filtered['Response Time'].str.contains('LOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Response Time'].str.contains('HIGH')
    counter2 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    return counter1, counter2

def noStressRT():
    counter1 = 0
    counter2 = 0
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/results1.csv')
    finalRows = df.tail(500)
    filtered = finalRows[finalRows.Stress.isnull()]
    boolFiltered = filtered['Response Time'].str.contains('LOW')
    counter1 = boolFiltered.sum()
    boolFiltered = filtered['Response Time'].str.contains('HIGH')
    counter2 = boolFiltered.sum()
    print(counter1)
    print(counter2)
    return counter1, counter2



# angryStressRT()
# anxiousStressRT()
# noStressRT()


#----------------------------------------------------------------------------------------------------------------------

def realTimeAccProb1():
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/resultsA.csv')
    steps = df["Step"]
    accProb = df["Accident Probability"]
    return steps, accProb

def realTimeAccProb2():
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/resultsB.csv')
    steps = df["Step"]
    accProb = df["Accident Probability"]
    return steps, accProb

def realTimeAccProb3():
    df = pd.read_csv('/home/dgarcia/TFG/Documentation/resultsC.csv')
    steps = df["Step"]
    accProb = df["Accident Probability"]
    return steps, accProb