## 250920750 Firas Aboushamalah

#empty lists for storing volume values
cubeList = []
ellipsoidList = []
pyramidList = []
inpShape = input("Please enter a valid shape ('cube', 'pyramid', 'ellipsoid', or 'quit' to end) ")

#begin loop
while True:
    if inpShape == "cube" or inpShape == "pyramid" or inpShape == "ellipsoid":
        #**FOR CUBE**
        if inpShape == "cube":
            while inpShape == "cube": #while the input value for the shape is cube keep doing this loop
                def cubeVolume(sideLength): #function for the cube volume
                    CUBE_VOLUME = round((sideLength ** 3), 1)  #sidelength x sidelength x sidelength
                    cubeList.append(CUBE_VOLUME)  #add the volume to the list cubeVolumes
                    cubeList.sort()  #makes list smallest to largest
                    print("The volume of a cube with a side length of {} is {}".format(sideLength, CUBE_VOLUME))  #print calculation to the screen
                    print("")
                sideLength = (input("Enter the side length or quit: "))  #loop to keep asking the user for more values until they choose quit
                if sideLength == "quit":  #quit the shape and ask the user if they want to do the other two shapes or end to print the summary
                    inpShape = input("Enter pyramid or ellipsoid or end to exit program: ")  #quit cube, ask other shapes or end to exit program
                    print("")
                    if inpShape == "end":  #print the lists and exit program
                        print("")
                        print("Cube:", cubeList)
                        print("Pyramid:", pyramidList)
                        print("Ellipsoid:", ellipsoidList)
                        quit()
                else:
                    cubeVolume(float(sideLength))  #if they don't enter quit, call function and loop
        #**FOR PYRAMID**
        if inpShape == "pyramid":
            while inpShape == "pyramid":
                def pyramidVolume(heightLength, baseLength): #call pyramid function
                    PYRAMID_VOLUME = round((((baseLength**2) * heightLength) / 3), 1)  #store the volume in volume2 (volume is cube)
                    pyramidList.append(PYRAMID_VOLUME)  #store volume result in pyramid list
                    pyramidList.sort()  #arrange the list values in ascending order
                    #print the calculation result
                    print("The volume of a pyramid with a base of {} and a height of {} is {}".format(baseLength, heightLength, PYRAMID_VOLUME))
                    print("")
                heightLength = input("Input value for height or quit: ") #enter height value or quit to exit shape
                if heightLength == "quit":  #quit the pyramid shape and ask user if they want to enter another shape or exit program and print summary
                    inpShape = input("Enter cube or ellipsoid or end to exit program: ")
                    print("")
                    if inpShape == "end": #print the lists and exit program
                        print("Cube:", cubeList)
                        print("Pyramid:", pyramidList)
                        print("Ellipsoid:", ellipsoidList)
                        quit()
                else:
                    baseLength = input("Input value for base length or quit: ") #enter base valueor quit to exit the shape
                    #if user quits during loop for second value
                    if baseLength == "quit": #exit the shape
                        inpShape = input("Enter cube or ellipsoid or end to exit program: ")  #and ask if user wants to enter new shape or exit progarm and print summary
                        if inpShape == "end": #print the lists and exit program
                            print("Cube:", cubeList)
                            print("Pyramid:", pyramidList)
                            print("Ellipsoid:", ellipsoidList)

                    pyramidVolume(float(heightLength), float(baseLength)) #calling function
        #**FOR ELLIPSOID**
        if inpShape == "ellipsoid":
            while inpShape == "ellipsoid": #while the input shape value remains ellipsoid, keep looping
                def ellipsoidVolume(radius1, radius2, radius3): #parameters for each radius
                    import math #get math module to use pi
                    ELLIPSOID_VOLUME = round((4/3 * math.pi * radius1 * radius2 * radius3), 1) #math.pi = value of pi imported from .math
                    ellipsoidList.append(ELLIPSOID_VOLUME) #add volume to ellipsoid list
                    ellipsoidList.sort() #sort list ascending order
                    #print calculation result
                    print("The volume of an ellipsoid with radius {}, {} and {} is {}".format(radius1, radius2, radius3, ELLIPSOID_VOLUME))
                    print("")

                radius1 = input("Enter a value for radius 1 or quit: ")  #enter a value for the first radius or quit to exit shape
                if radius1 == "quit":  #if quit is entered, exit the shape
                    inpShape = input("Enter cube or pyramid or end to exit program: ") #ask user to enter a new shape or end to exit the progarm and print summary
                    if inpShape == "end": #print summary and exit program
                        print("")
                        print("Cube:", cubeList)
                        print("Pyramid:", pyramidList)
                        print("Ellipsoid:", ellipsoidList)
                        quit() #exits
                else:
                    radius2 = input("Enter a value for radius 2: ")  #enter a value for the first radius or quit to exit shape
                    if radius2 == "quit":  #if quit is entered, exit the shape
                        inpShape = input("Enter cube or pyramid or end to exit program: ")  #ask user to enter a new shape or end to exit the progarm and print summary
                        if inpShape == "end":  #print summary and exit program
                            print("")
                            print("Cube:", cubeList)
                            print("Pyramid:", pyramidList)
                            print("Ellipsoid:", ellipsoidList)
                            quit() #exit
                    else:
                        radius3 = input("Enter a value for radius 3: ")  #enter a value for the first radius or quit to exit shape
                        if radius3 == "quit":  #if quit is entered, exit the shape
                            inpShape = input("Enter cube or pyramid or end to exit program: ")  #ask user to enter a new shape or end to exit the progarm and print summary
                            if inpShape == "end":  #print summary and exit program
                                print("")
                                print("Cube:", cubeList)
                                print("Pyramid:", pyramidList)
                                print("Ellipsoid:", ellipsoidList)
                                quit() #exit

                        ellipsoidVolume(float(radius1), float(radius2), float(radius3)) #call the function
#
#
#
#### IF USER ENTERS 'QUIT' IN FIRST SHAPE, EXIT PROGARM
    elif inpShape == "quit":
        print("")
        print("You have come to the end of the session.\nYou did not perform any volume calculations.") #print no calculations made
        quit()  #exit program
    #### IF USER ENTERS AN INVALID INPUT FIRST
    elif inpShape != "cube" or inpShape != "pyramid" or inpShape != "ellipsoid" or inpShape != "quit": #if neither of the following which are valid inputs
        print("")
        print("Not a valid option. Valid options are 'cube', 'pyramid', 'ellipsoid', or 'quit'.")
        inpShape = input("Please enter a valid shape ('cube', 'pyramid', 'ellipsoid', or 'quit' to end) ")








