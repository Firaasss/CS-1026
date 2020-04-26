userInput = input("Enter file name: ")
openFile = open(userInput, "r")
lines = 0
words = 0
characters = 0

for line in openFile:
    lines = lines + 1
    word = line.split()
    for i in word:
        words = words + 1
        for char in i:
            characters = characters + 1

print("Number of lines is {} and words is {} and characters is {}".format(lines, words, characters))
