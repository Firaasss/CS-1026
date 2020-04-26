#reads numbers, adds them to list if not already in list. When list has 10 numbers, program displays contents/quits

numList = []

while len(numList) < 4:
    numbers = int(input("Enter a number: "))

    if numbers not in numList:
        numList.append(numbers)



numList.sort()

print(numList)
