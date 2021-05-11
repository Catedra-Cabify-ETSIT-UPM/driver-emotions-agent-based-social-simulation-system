#Big Five personality dimensions to determine driving styles: Extraversion, Agreeableness, Conscientiousness, Neuroticism, Openness

def evaluatePersonality(self, personality):
    #Personality values 
    extraversion = personality[0]  
    agreeableness = personality[1]
    conscientiousness = personality[2]
    neuroticism = personality[3]
    openness = personality[4] 

    #Check reckless driving style 
    if (extraversion == 1 and agreeableness == 0 and conscientiousness == 0 and neuroticism == 1 and openness == -1):
        drivingStyle = "RECKLESS"
        return drivingStyle
    #Check anxious driving style 
    elif (extraversion == -1 and agreeableness == 0 and conscientiousness == 0 and neuroticism == 1 and openness == 1):
        drivingStyle = "ANXIOUS"
        return drivingStyle
    #Check angry driving style 
    elif (extraversion == -1 and agreeableness == 0 and conscientiousness == 0 and neuroticism == 1 and openness == 0):
        drivingStyle = "ANGRY"
        return drivingStyle
    #Check careful driving style 
    elif (extraversion == 1 and agreeableness == 1 and conscientiousness == 1 and neuroticism == 0 and openness == 1):
        drivingStyle = "CAREFUL"
        return drivingStyle

    else: 
        return "NO DRIVING STYLE"

