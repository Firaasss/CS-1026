from random import randint
listA = []
for i in range(10): #filling list
    value = randint(1, 100)
    listA.append(value)

def evenPosition(values): #even indexes
    for i in range(0, len(values), 2):
        print(values[i], end=" | ")
    print()

def evens(values): #even values
    for i in range(0, len(values)):
        if values[i] % 2 == 0:
            print(values[i], end=" | ")
    print()

def reverse(values): #print in reverse order
    i = len(values) - 1
    while i > -1:
        print(values[i], end=" | ")
        i = i - 1
    print()

def firstLast(values): #only first and last values
    print(values[0], "and", values[-1])

evenPosition(listA)
evens(listA)
reverse(listA)
firstLast(listA)
