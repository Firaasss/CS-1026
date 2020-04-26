###############################################################################################
# Firas Aboushamalah      #####################################################################
# 250 920 750             #####################################################################
# CS1026b Assignment #3   #####################################################################
# Happy Score Calculator  #####################################################################
###############################################################################################

import happy_histogram #import happy histogram from file

happinessValues = [] #empty list to store keywords from text file

try:
    fileInput = input("Enter a file name for keywords: ")  #if keywords entered, go through, if not raise exception error
    keywordFile = open(fileInput, "r",encoding="utf-8")  #opening file
    for line in keywordFile:  #loop going through each line in keywords
        entries = line.split(",")  #splitting each line at space
        value = int(entries[1].strip("\n"))  #removing \n from the second element in line and declaring the second value
        entries = entries[0]  #declaring the first value in the list (love, hate, etc.)
        happinessValues.append(entries) #adding the keyword to happinessValues list
        happinessValues.append(value)  #adding the value associated with the word to the happinessValues list

except IOError:  #raise error if anything other than "keywords" is entered.
    print("Error: file not found.")

##TIMEZONE VALUES
pacific = 0  #happy score for pacific
pacificKeywords = 0  #number keywords in pacific
pacificTweets = 0  #number total tweets in pacific
ssPacific = 0  #sentiment score pacific

mountain = 0  #final happy score for mountain
mountainKeywords = 0  #number keywords in mountain
mountainTweets = 0  #number total tweets in mountain
ssMountain = 0  #sentiment score mountain

central = 0  #happy score for central
centralKeywords = 0  #number keywords in central
centralTweets = 0  #number total tweets in central
ssCentral = 0  #sentiment score central

eastern = 0  #happy score for eastern
easternKeywords = 0  #number keywords in eastern
easternTweets = 0  #number total tweets in eastern
ssEastern = 0  #sentiment score Eastern

##CONSTANTS FOR THE REGION LAT AND LONGS##
P1 = [49.189787, -67.444574]
P2 = (24.660845, -67.444574)
P3 = (49.189787, -87.518395)
P4 = (24.660845, -87.518395)
P5 = (49.189787, -101.998892)
P6 = (24.660845, -101.998892)
P7 = (49.189787, -115.236428)
P8 = (24.660845, -115.236428)
P9 = (49.189787, -125.242264)
P10 = (24.660845, -125.242264)

try:  #opening tweets file
    file2Input = input("Enter file name for tweets: ")
    tweetFile = open(file2Input, "r",encoding="utf-8")
    for line in tweetFile:  #loop to examine each line in file
        tweet = line.split(' ', 5)  #split at the space with 5 splits (split lat, long, number, date, time and words)
        #####LAT AND LONG#####
        lat = tweet[0].lstrip('[') #strips [
        lat = lat.rstrip(",") #strips [
        long = tweet[1].rstrip("]") # strips ]
        lat = float(lat) # assigning lat
        long = float(long) # assigning long
        #######################
        singleWord = tweet[5].split(" ") #in the word portion of the tweet, split at the spaces to get individual word
        if P2[0] <= lat <= P1[0]: # checks if the lat region of the tweet is in any region
            if P3[1] < long <= P2[1]: # checks long of tweet if in eastern region
                easternTweets = easternTweets + 1  #if tweet falls in region, add 1 to tweet counter
                for alpha in range(0, len(singleWord)):  #loop going from beginning to end of words in tweet
                    word = singleWord[alpha].lower()  #make them all lowercase to match ones in happinessValues
                    word = word.strip("!@#$%^&*(),.?';:")  #remove punctuation so it doesn't interfere when checking similariies
                    if word in happinessValues:  #check if word is in happinessValues list
                        easternKeywords = easternKeywords + 1  #add one to counter of same keywords in each list
                        positionValue = happinessValues.index(word) + 1  #find index of word occuring in happinessValues is and add 1 to get the value of the word
                        ssEastern = ssEastern + happinessValues[positionValue]  #get sentiment score
                        eastern = round((ssEastern / easternKeywords), 2) #compute total happiness score for region
            ##
            elif P5[1] < long <= P4[1]: # checks long of tweet if in central region
                centralTweets = centralTweets + 1  #if tweet falls in region, add 1 to tweet counter
                for alpha in range(0, len(singleWord)):  #loop going from beginning to end of words in tweet
                    word = singleWord[alpha].lower()  #make them all lowercase to match ones in happinessValues
                    word = word.strip("!@#$%^&*(),.?';:")  #remove punctuation so it doesn't interfere when checking similariies
                    if word in happinessValues:  #check if word is in happinessValues list
                        centralKeywords = centralKeywords + 1  #add one to counter of same keywords in each list
                        positionValue = happinessValues.index(word) + 1  #find index of word occuring in happinessValues is and add 1 to get the value of the word
                        ssCentral = ssCentral + happinessValues[positionValue]  #get sentiment score
                        central = round((ssCentral / centralKeywords), 2) #compute total happiness score for region
            ##
            elif P7[1] < long <= P6[1]:# checks long of tweet if in mountain region
                mountainTweets = mountainTweets + 1  #if tweet falls in region, add 1 to tweet counter
                for alpha in range(0, len(singleWord)):  #loop going from beginning to end of words in tweet
                    word = singleWord[alpha].lower()  #make them all lowercase to match ones in happinessValues
                    word = word.strip("!@#$%^&*(),.?';:")  #remove punctuation so it doesn't interfere when checking similariies
                    if word in happinessValues:  #check if word is in happinessValues list
                        mountainKeywords = mountainKeywords + 1  #add one to counter of same keywords in each list
                        positionValue = happinessValues.index(word) + 1  #find index of word occuring in happinessValues is and add 1 to get the value of the word
                        ssMountain = ssMountain + happinessValues[positionValue]  #get sentiment score
                        mountain = round((ssMountain / mountainKeywords), 2) #compute total happiness score for region
            ##
            elif P9[1] < long <= P8[1]:# checks long of tweet if in pacific region
                pacificTweets = pacificTweets + 1  #if tweet falls in region, add 1 to tweet counter
                for alpha in range(0, len(singleWord)):  #loop going from beginning to end of words in tweet
                    word = singleWord[alpha].lower()  #make them all lowercase to match ones in happinessValues
                    word = word.strip("!@#$%^&*(),.?';:")  #remove punctuation so it doesn't interfere when checking similariies
                    if word in happinessValues:  #check if word is in happinessValues list
                        pacificKeywords = pacificKeywords + 1  #add one to counter of same keywords in each list
                        positionValue = happinessValues.index(word) + 1  #find index of word occuring in happinessValues is and add 1 to get the value of the word
                        ssPacific = ssPacific + happinessValues[positionValue]  #get sentiment score
                        pacific = round((ssPacific / pacificKeywords), 2)  #compute total happiness score for region
    #PRINT SCORES AND THEIR TWEETS
    print("")
    print("Eastern Score: {} with {} tweets".format(eastern, easternTweets))
    print("Central Score: {} with {} tweets".format(central, centralTweets))
    print("Mountain Score: {} with {} tweets".format(mountain, mountainTweets))
    print("Pacific Score: {} with {} tweets".format(pacific, pacificTweets))
    #Call happy histogram function to get graphic file
    happy_histogram.drawSimpleHistogram(eastern,central,mountain,pacific)
except IOError: #raises error if "tweets" is typed incorrectly
    print("Error: file not found.")
