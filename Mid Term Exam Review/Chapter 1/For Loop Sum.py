#ask user for a positive number and sums up all even numbers between 0 and that number.

total = 0
number = int(input("Enter a positive number: "))

for i in range(0, number + 1, 2):
    total = total + i
print(total)




