inputOpen = open("input.txt", "r")
outputOpen = open("output.txt", "w")
for line in reversed(list(inputOpen)):
    outputOpen.write(line)

inputOpen.close()
outputOpen.close()
