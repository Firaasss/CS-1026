positive = []
neutral = []
negative = []

stringystring = "I really am very happy for you I love the weather I am also sad and have some regrets about being so tired"

file = open("keywords", "r")
for line in file:
    entries = line.split(",")
    value = int(entries[1].strip("\n"))
    if value == 20:
            positive.append(entries[0])
    elif value == 0:
        neutral.append(entries[0])
    elif value == -10:
        negative.append(entries[0])
    print(entries)

value = 0

tweet = stringystring.split()
for word in tweet:
    if word in positive:
        value = value + 20
    elif word in neutral:
        value = value
    elif word in negative:
        value = value - 10
    print(value)





