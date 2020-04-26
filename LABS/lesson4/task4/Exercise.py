intNumbers = int(input("How many numbers do you want to use? "))
total = 0
for i in range(intNumbers):
    numbers = int(input("Please enter each number"))
    total = total + numbers
    if i == 0:
        min=numbers
        max=numbers
    else:
        if numbers < min:
            min=numbers
        if numbers > max:
            max=numbers






average = total / intNumbers
print("The average of the numbers is",average,)


