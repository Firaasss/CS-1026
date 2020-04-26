def main():

    result1 = cubeVolume(3)
    result2 = cubeVolume(5)
    print("Result1 has volume of", result1)
    print("Result2 is", result2)


def cubeVolume(sideLength):
    volume = sideLength**3
    return volume

main()





