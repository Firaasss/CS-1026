def smallest(x, y, z):
    if x < y and x < z:
        smallest = x
        print("The smallest number is: ", smallest)
    elif y < x and y < z:
        smallest = y
        print("The smallest number is: ", smallest)
    else:
        print("The smallest number is: ", smallest)

smallest(12, 9, 15)
