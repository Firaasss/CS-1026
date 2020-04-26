import happy_histogram
happinessValues = []
try:
    fileInput = input("Enter a file name for keywords: ")
    keywordFile = open(fileInput, "r",encoding="utf-8")
    for line in keywordFile:
        entries = line.split(",")
        value = int(entries[1].strip("\n"))
        entries = entries[0]
        happinessValues.append(entries)
        happinessValues.append(value)
except IOError:
    print("Error: file not found.")

##TIMEZONE VALUES
pacific = 0  #happy score for pacific
pacificKeywords = 0  #number keywords in pacific
countPacific = 0  #number total tweets in pacific
ssPacific = 0  #sentiment score pacific

mountain = 0  #final happy score for mountain
mountainKeywords = 0  #number keywords in mountain
countMountain = 0  #number total tweets in mountain
ssMountain = 0  #sentiment score mountain

central = 0  #happy score for central
centralKeywords = 0  #number keywords in central
countCentral = 0  #number total tweets in central
ssCentral = 0  #sentiment score central

eastern = 0  #happy score for eastern
easternKeywords = 0  #number keywords in eastern
countEastern = 0  #number total tweets in eastern
ssEastern = 0  #sentiment score Eastern
#empty lists so program stores values inside loops
lat = []
long = []
tweet = []
try:
    file2Input = input("Enter file name for tweets: ")
    tweetFile = open(file2Input, "r",encoding="utf-8")
    for line in tweetFile:
        tweet = line.split()
        for i in range(0,len(tweet)):
            word = tweet[i].lower()
            word = word.strip("!@#$%^&*(),.?';:") # strips punctuation
            tweetLine = line.split(", ") # splits each line in tweet file at comma space
            lineLeftStrip = tweetLine[0].strip("[") #strips [
            tempString = tweetLine[1].strip("]") # strips ]
            tempString_1 = tempString.strip("[") # strips [ again
            lineRightStrip = tempString_1.split("] ") # strips ] space
            lat = float(lineLeftStrip) # assigning lat
            long = float(lineRightStrip[0]) # assigning long
            #region=zone(lat,long)
            ####### IF LAT IS WITHIN PARAMETERS #######
        if lat >= 24.660845 and lat <= 49.189787: # checks if the lat region of the tweet is in any region
            if -87.518395 < long and long <= -67.444574: # checks long of tweet if in eastern region
                countEastern = countEastern + 1 #add tweets
                if word in happinessValues:
                    easternKeywords = easternKeywords + 1 #add keywords
                    positionValue = int(happinessValues.index(word)) + 1
                    print(word, positionValue)
                    ssEastern = ssEastern + int(happinessValues[positionValue])
                    eastern = ssEastern / easternKeywords
            elif -101.998892 < long and long <= -87.5183952: # checks long of tweet if in central region
                countCentral = countCentral + 1 #add tweets
                if word in happinessValues:
                    centralKeywords = centralKeywords + 1 #add keywords
                    positionValue = happinessValues.index(word) + 1
                    ssCentral = ssCentral + happinessValues[positionValue]
                    central = ssCentral / centralKeywords
            elif -115.236428 < long and long <= -101.998892:# checks long of tweet if in mountain region
                countMountain = countMountain + 1 #add tweets
                if word in happinessValues:
                    mountainKeywords = mountainKeywords + 1 #add keywords
                    positionValue = happinessValues.index(word) + 1
                    ssMountain = ssMountain + happinessValues[positionValue]
                    mountain = ssMountain / mountainKeywords
            elif -125.242264 < long and long <= -115.236428:# checks long of tweet if in pacific region
                countPacific = countPacific + 1 #add tweets
                if word in happinessValues:
                    pacificKeywords = pacificKeywords + 1 #add keywords
                    positionValue = happinessValues.index(word) + 1
                    ssPacific = ssPacific + happinessValues[positionValue]
                    pacific = ssPacific / pacificKeywords
    #SCORES/TWEETS#
    print("Eastern Score: {} with {} tweets".format(eastern, countEastern))
    print("Central Score: {} with {} tweets".format(central, countCentral))
    print("Mountain Score: {} with {} tweets".format(mountain, countMountain))
    print("Pacific Score: {} with {} tweets".format(pacific, countPacific))
    #GRAPHIC ASPECT#
    happy_histogram.drawSimpleHistogram(eastern,central,mountain,pacific)
except IOError:
    print("Error: file not found.")
