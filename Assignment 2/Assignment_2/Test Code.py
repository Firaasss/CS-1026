#########
#
#
#  TESTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT######################
#empty lists for storing volume values
cubeList = []
ellipsoidList = []
pyramidList = []

#prompt user for input for the shape
inpShape = input("Please enter a valid shape ('cube', 'pyramid', 'ellipsoid', or 'quit' to end) ")
#list containing the valid inputs
validShapes = ["cube", "pyramid", "ellipsoid"]

#begin loop
while True:
    #**FOR CUBE**
    if inpShape == "cube":
        def cubeVolume(sideLength):
            CUBE_VOLUME = round((sideLength ** 3), 1) #sidelength x sidelength x sidelength
            cubeList.append(CUBE_VOLUME) #add the volume to the list cubeVolumes
            cubeList.sort() #makes list smallest to largest
            print("The volume of a cube with a side length of {} is {}".format(sideLength, CUBE_VOLUME)) #print calculation to the screen
        print("") #empty line
        sideLength = (input("Input the side length: ")) #loop to keep asking the user for more values until they choose quit
        if sideLength == "quit":
            print("")
            print("The accumulated volumes for cube are:", cubeList)
            break
        else:
            cubeVolume(float(sideLength))
    #**FOR PYRAMID**
    elif inpShape == "pyramid":
        def pyramidVolume(heightLength, baseLength):
            PYRAMID_VOLUME = round((((baseLength**2) * heightLength) / 3), 1)  #store the volume in volume2 (volume is cube)
            pyramidList.append(PYRAMID_VOLUME) #store volume result in pyramid list
            pyramidList.sort() #arrange the list values in ascending order
            #print the calculation result
            print("The volume of a pyramid with a base of {} and a height of {} is {}".format(baseLength, heightLength, PYRAMID_VOLUME))
            print("") #blank line
        heightLength = input("Input value for height or quit: ")
        #if user quits during loop for first value
        if heightLength == "quit":
            print("")
            print("The accumulated volumes for pyramid are: ", pyramidList) #print complete list at the end
            break
        else:
            baseLength = input("Input value for base length or quit: ")
            #if user quits during loop for second value
            if baseLength == "quit":
                print("")
                print("The accumulated volumes for pyramid are: ", pyramidList) #print complete list at end
                break
            pyramidVolume(float(heightLength), float(baseLength)) #calling function
    #**FOR ELLIPSOID**
    elif inpShape == "ellipsoid":
        import math #get math module to use pi
        def ellipsoidVolume(radius1, radius2, radius3):
            ELLIPSOID_VOLUME = round((4/3 * math.pi * radius1 * radius2 * radius3), 1) #math.pi = value of pi imported from .math
            ellipsoidList.append(ELLIPSOID_VOLUME) #add volume to ellipsoid list
            ellipsoidList.sort() #sort list ascending order
            #print calculation result
            print("The volume of an ellipsoid with radius {}, {} and {} is {}".format(radius1, radius2, radius3, ELLIPSOID_VOLUME))
            print("")
        radius1 = input("Enter a value for radius 1: ")
        #if user quits during loop for first value:
        if radius1 == "quit":
            print("")
            print("The accumulated volumes for ellipsoid rae: ", ellipsoidList) #print complete list
            break
        radius2 = input("Enter a value for radius 2: ")
        #if user quits during loop for second value:
        if radius2 == "quit":
            print("")
            print("The accumulated volumes for ellipsoid rae: ", ellipsoidList) #print complete list
            break
        #if user quits during loop for third value:
        radius3 = input("Enter a value for radius 3: ")
        if radius3 == "quit":
            print("")
            print("The accumulated volumes for ellipsoid rae: ", ellipsoidList) #print complete list
            break
        ellipsoidVolume(float(radius1), float(radius2), float(radius3))
#
#
#
#### IF USER ENTERS 'QUIT' FIRST
    elif inpShape == "quit":
        print("")
        print("You have come to the end of the session.\nYou did not perform any volume calculations.")
        quit()
#### IF USER ENTERS AN INVALID INPUT FIRST
    else:
        print("")
        print("Not a valid option. Valid options are 'cube', 'pyramid', 'ellipsoid', or 'quit'.")
        inpShape = input("Please enter a valid shape ('cube', 'pyramid', 'ellipsoid', or 'quit' to end) ")








