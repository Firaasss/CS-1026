values = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def multiply(values, number):
    for i in range(len(values)):
        values[i] = values[i] * number
    return values
number = int(input("Enter a number"))
print(multiply(values, number))
