##exercise

num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))
num3 = int(input("Please enter the last number: "))

if (num1 < num2) and (num2 < num3):
    print("Ascending.")
elif (num1 > num2) and (num2 > num3):
    print("Descending.")
else:
    print("Not in order")

###########################################################




