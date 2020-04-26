## User inputs 2 numbers and program will operate on them

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

sumNumbers = num1 + num2
print("The sum of the two numbers is {}".format (sumNumbers))

prodNumbers = num1 * num2
print("The product of the two numbers is {}".format (prodNumbers))
print("")
#reinputting 2 numbers to find difference with abs
num1 = float(input("Now, to find the distance, enter another number: "))
num2 = float(input("And the second number: "))
diffNumbers = abs(num1 - num2) #gives the result a positive number
print("The difference between the two numbers is {}.".format (diffNumbers))
print("")
#this will find the average of two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sumNumbers = num1 + num2
avgNumbers = (sumNumbers) / 2
print("The average of the two numbers is {}".format(avgNumbers))
maxNumbers = max(num1, num2)
print("The max of the two numbers is {}".format(maxNumbers))



