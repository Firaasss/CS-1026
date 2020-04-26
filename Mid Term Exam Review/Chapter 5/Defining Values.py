x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))
def smallest(x, y, z):
    if x < y and x < z:
        return x
    elif y < x and y < z:
        return y
    else:
        return z

print(smallest(x, y, z))




