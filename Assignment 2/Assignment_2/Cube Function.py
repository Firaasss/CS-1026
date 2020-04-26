cubeVolumes = []

def cubeVolume(sideLength):
    volume = round((sideLength ** 3), 1) #sidelength x sidelength x sidelength
    cubeVolumes.append(volume) #add the volume to the list cubeVolumes
    cubeVolumes.sort() #makes list smallest to largest
    print("Cube:", cubeVolumes) #print the list to the screen
sideLength = (input("Input the side length: ")) #loop to keep asking the user for more values until they choose quit
if sideLength == "quit":
    print("")
    print("The accumulated volumes for cube are:", cubeVolumes)
    break
else:
    cubeVolume(float(sideLength))
