def allTheSame(x,y,z):
    if x == y and x == z:
        return True
    else:
        return False

x = int(input("Enter a value for x: "))
y = int(input("Enter a value for y: "))
z = int(input("Enter a value for z: "))
print(allTheSame(x,y,z))
