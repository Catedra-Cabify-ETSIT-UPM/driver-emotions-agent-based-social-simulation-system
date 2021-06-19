from numpy.random import choice
import configparser
import os
import math

dic = {'anger': '0', 'anxiety': '0', 'fear': '1', 'happiness': '0'}
if int(dic["fear"]) == 1:
    print("Siuh")

emotion = choice(("HAPPINESS", "FEAR", "ANGER", "ANXIETY"), 1, (0.25,0.25, 0.25, 0.25))
e = emotion[0]
print(emotion[0])
config = configparser.ConfigParser()
config.read('general.ini')
Emotions = dict(config[e])
print(Emotions)




