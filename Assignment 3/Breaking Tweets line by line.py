happinessValues = ['love', 10, 'like', 5, 'best', 10, 'hate', 1, 'lol', 10, 'better', 10, 'worst', 1, 'good', 5, 'happy', 10, 'haha', 5, 'please', 5, 'great', 5, 'bad', 1, 'save', 5, 'saved', 5, 'pretty', 5, 'greatest', 10, 'excited', 10, 'tired', 1, 'thank', 5, 'amazing', 10, 'glad', 10, 'ruined', 1, 'negative', 1, 'loving', 10, 'sorry', 1, 'hurt', 1, 'alone', 1, 'sad', 1, 'positive', 5, 'regrets', 1, 'God', 5]
value = 0

tweets = open("Tweets", "r")
for line in tweets:
    tweetList = line.split()
    print(tweetList)
    for word in tweetList:
        if word in happinessValues:
            posValue = happinessValues.index(word) + 1
            value = value + happinessValues[posValue]
            print(word, value)






