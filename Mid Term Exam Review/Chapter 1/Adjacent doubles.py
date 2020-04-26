numbers = int(input("How many numbers u wanna do? "))

maxNum = 0
minNum = 0

for i in range(numbers):
    singleNums = int(input("Enter each number: "))
    if singleNums > maxNum:
        maxNum = singleNums
    elif singleNums < maxNum:
        minNum = singleNums

print("The max num is", maxNum)
print("The min num is", minNum)

