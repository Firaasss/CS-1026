########################################################################################
############################## 1026 ASSIGNMENT 4: CLASSES ##############################
###########################        FIRAS ABOUSHAMALAH        ###########################
##############################       250 - 920 - 750      ##############################
########################################################################################

class Country:

    def __init__(self, name, pop, area, continent):
        #INSTANCE VARIABLES
        self._name = name
        self._pop = pop
        self._area = area
        self._continent = continent

        #GETTERS
    def setPopulation(self, pop):
        self._pop = pop  #returns the set population

    def getName(self):
        return self._name  #returns the country name

    def getArea(self):
        return self._area  #returns the area surrounding the country

    def getPopulation(self):
        return self._pop  #returns the population of the country

    def getContinent(self):
        return self._continent  #returns continent of country

    def getPopDensity(self):
        return float(("%.2f" % (self._pop / self._area)))  #returns pop density rounded to 2 decimal points

    def __repr__(self):
        return self._name + " in " + self._continent  #overloads the class to return the values of country name + continent

class CountryCatalogue:  #initiate second class

    def __init__(self, fileOpen):  #fileopen parameter is to pass data.txt file

        openDictionary = open("continent.txt", "r")  #open continent file
        self._cDictionary = dict()  #initialize dictionary for cDictionary instance
        readContinents = openDictionary.readlines()[1:]   #get rid of header in file
        for line in readContinents:  #for loop to edit contents of Continents
            dataContinents = line.rstrip("\n")  #remove \n from end
            stripContinents = dataContinents.split(",")  #break at comma
            continent = stripContinents[1]  #declare continent value
            country = stripContinents[0]  #declare country value
            self._cDictionary[country] = continent  #fill cDictionary with country name as key and continent as value

        openDictionary.close()  #close file

        openCatalogue = open(fileOpen, "r")  #open "data.txt" or whatever you pass through parameter
        self._catalogue = dict()    #initialize dictionary for catalogue instance

        readCountries = openCatalogue.readlines()[1:]  #get rid of header in file
        for line in readCountries:  #for loop to edit contents of file
            dataCountries = line.rstrip("\n")  #remove \n from end of line
            stripCountries = dataCountries.split("|")  #split at the |
            name = stripCountries[0]  #declare value for name
            pop = int(stripCountries[1].replace(",", ""))  #declare value for population
            area = float(stripCountries[2].replace(",", "".replace(",", "")))  #declare value for area
            country = Country(name, pop, area, self._cDictionary[name])  #contents are all stored in country variable
            self._catalogue[name] = country  #fill catalogue dictionary with country name as key and its contents as the value

    def addCountry(self):  #method to add new country to the dictionary
        var = True  #set a stationary variable to perform execution as long as it is true
        while var is True:
            addCountry = input("What country would you like to add? ")  #user input country name
            if addCountry in self._cDictionary:  #if user input is already matched in the dictionary
                print("Your country already exists. Try another.")  #country exists, raise error message and reloop
            else:  #if country is not in dictionary
                var = False  #get out of while loop and perform rest of execution below
        addPopulation = int(input("What is the population of your country? "))  #ask for population of country
        addArea = float(input("What is the area of your country? "))  #ask for area of country
        addContinent = input("What continent is your country part of? ")  #ask for continent country is in
        callCountry = Country(addCountry, addPopulation, addArea, addContinent)  #put all the user inputted information in the call variable while calling class Country
        self._catalogue[addCountry] = callCountry  #input callCountry contents into self._catalogue by making it value and user-inputted country name as key
        self._cDictionary[addCountry] = addContinent  #add the country and continent to the cDictionary
        print("")  #empty line
        print("The country has been added.")

    def deleteCountry(self):  #method to remove countries from dictionary
        countryName = input("Enter the name of country you would like to delete: ")  #enter name of country to remove
        if countryName in self._catalogue:  #check to see if it is in the dictionary
            self._catalogue.pop(countryName)  #if it is remove the country
            print("")
            print("The country has been removed")
        else:  #if country name is not in the dictionary raise error message
            print("The country does not exist in the catalogue")

    def findCountry(self):  #method to list all information associated with country searched
        countryName = input("Enter the name of the country: ")  #enter name of country
        if countryName in self._catalogue:  #check to see if it is in dictionary
            print("Name:", self._catalogue[countryName].getName())  #list the country's name
            print("Continent:", self._catalogue[countryName].getContinent())  #continent it is in
            print("Area:", self._catalogue[countryName].getArea())  #area it is in
            print("Population:", self._catalogue[countryName].getPopulation())  #population it is in
            print("Population Density:", self._catalogue[countryName].getPopDensity())  #population density
        else:  #if country is not in dictionary
         print("Sorry! ", countryName, " is not in our catalogue.")  #raise error

    def filterCountriesByContinent(self):  #method to list countries in a certain continent
        inputContinent = input("Enter a continent you want to search countries in: ")  #enter name of continent
        for continent in self._cDictionary.items():  #for loop to check if continent is in values of dictionary
            if continent[1] == inputContinent:  #if it checks out
                print(continent[0])  #print the country associated with the continent

    def printCountryCatalogue(self):  #print the list of countries and continents using repr method
        for country in sorted(self._catalogue.values(), key=Country.getName):  #call Country class to use repr override method to get the values of country name and continent
            print(country)  #print country in for loop

    def setPopulationOfASelectedCountry(self):  #modify the population in a country
        var = True  #set a stationary variable
        while var is True:  #while it is true, go through loop
            askCountry = input("What country's population do you want to modify? ")
            if askCountry not in self._cDictionary:  #if the user inputted country is not in the dictionary, raise error
                print("This country is not in the list.")
            else:
                var = False  #if it is in dictionary, change var to false to continue with execution
                askPop = int(input("What is the country's new population?: "))  #enter new population - made into int
                self._catalogue[askCountry].setPopulation(askPop)  #use setPopulation method to update the pop to whatever user inputs
                print("")  #blank line
                print("The population density of the modified country is", self._catalogue[askCountry].getPopDensity())  #print updated population density

    def findCountryWithLargestPop(self):  #display name of country with largest population to screen
        popValues = sorted(self._catalogue.values(), key=Country.getPopulation)  #search in catalogue values using Country class for population values. Sorted to go from lowest to highest
        print("The country with the largest population is", popValues[-1].getName()) #-1 to get the last element in the sorted values which is highest population

    def findCountryWithSmallestArea(self):  #display name of country with smallest area to screen
        areaValues = sorted(self._catalogue.values(), key=Country.getArea)  #search in catalogue values using Country class for area values. Sorted to go from low to high
        print("Country with smallest Area:", areaValues[0].getName())  #Get first element in the sorted array which is the lowest area

    def filterCountriesByPopDensity(self):  #method for users to enter range of pop density and lists countries within it
        lowerBound = float(input("Enter the lower bound for the population density range: "))  #enter lowest population density
        upperBound = float(input("Enter the upper bound for the population density range: "))  #enter highest population density
        for i in self._catalogue.values():  #for each element in the catalogue values
            if lowerBound < i.getPopDensity() < upperBound:  #all countries with population density between lowest and highest input values
                print(i.getName())  #getter method to print name of the countries in the for loop

    def findMostPopulousContinent(self):  #display name of continent with most # of people living in it and how many people living in it
        dictContinents = dict()  #return dictionary object
        listContinents = set()  #returns set object
        for i in self._catalogue.values():  #for loop to check values in catalogue
            listContinents.add(i.getContinent())  #add the populations of the continents to the set

        for continent in listContinents:  #for each in the list Continents object
            dictContinents[continent] = list()  #returns a list object for dictContinents variable

        for country in self._catalogue.values():  #for each in the catalogue values
            dictContinents[country.getContinent()].append(country.getPopulation())  #appending population to the new list

        dictPopulation = dict()  #
        for key in dictContinents.keys():
            dictPopulation[key] = sum(dictContinents[key])

        MAX = 0  #initialize a constant called max valued at 0
        NAME = ""  #empty constant to store the name of continent with most people
        for c in dictPopulation.keys():  #for loop for elements in the dictPopulation dictionary's keys (not values)
            if dictPopulation[c] > MAX:  #if the population is greater than MAX
                MAX = dictPopulation[c]  #update max to whatever the population is
                NAME = c  #update the NAME to whichever continent has the most population
        print('The most populous continent is', NAME, 'with', dictPopulation[NAME], 'people')  #at end of reading all values, print continent with most population

    def saveCountryCatalogue(self, filename):  #save all countries to a file alphabetically
        self._out = open(filename, "w")  #open the user inputted file
        self._list = []  #create a list in the instance variable
        for i in sorted(self._cDictionary):  #for i in the dictionary (sorted)
            self._list.append(i)  #append the element to the list
        for element in self._list:  #for each element in the list
            for k in self._catalogue.values():  #for each k in values of catalogue
                if element == k.getName():  #check to see if the element is equal to the country name
                    self._list[self._list.index(element)] = k  #get index of the position element in list
        for key in self._list:  #for each element in the list
            self._out.write(key.getName() + "|" + key.getContinent() + "|" + str(key.getPopulation()) + "|" + str(key.getPopDensity()) + "\n")  #write these contents to the file
        print("The catalogue has been saved to", filename)  #print a finalization message confirming the catalogue was saved to the file name
        self._out.close()  #close the file after finishing operations
