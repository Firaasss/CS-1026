#reads temperature value and letter C for Celsius or F for FAhrenheit. Print if solid, liquid or gas at given temp.

temperatureValue = float(input("What is the temperature? "))
temperatureType = (input("Is it fahrenheit or celsius? (type f or c"))

if temperatureType is "f" :
    temperatureValue = (temperatureValue - 32) * 5/9
else :
    temperatureValue = temperatureValue, "c"
print(temperatureValue)




