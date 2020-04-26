# dkim628 Dohyun Kim 250921395

class Country :
    def __init__(self, name, population, area, continent):
        self._name = name
        self._population = population
        self._area = area
        self._continent = continent

    def __repr__(self):
        self._return = self._name + " in " + self._continent
        return self._return

    def setPopulation(self, pop):               # set the population
        self._population = pop

    def getName(self):                  # get the name
        return self._name

    def getArea(self):                  # get the area
        return self._area

    def getPopulation(self):            # get the population
        return self._population

    def getContinent(self):             # get the continent
        return self._continent

    def getPopDensity(self):            #get the popluation density
        return float(("%.2f"%(self._population / self._area)))         # calculating population density

class CountryCatalogue:

    def __init__(self,filename):
        dictionaryOpen = open("continent.txt", "r")
        self._cDictionary = dict()

        for line in dictionaryOpen:
            split = line.strip().split(",")         # splits the line
            self._cDictionary[split[0]] = split[1]          # inserts to the dictionary
        self._cDictionary.pop("Country")

        catalogueOpen = open(filename, "r")
        self._catalogue = []

        catalogueOpen.readline()
        for line in catalogueOpen:
            split = line.strip()            # strips the line
            split = split.split("|")        # splits the line
            self._catalogue.append(Country(split[0],int(split[1].replace(",","")),float(split[2].replace(",","")), self._cDictionary[split[0]]))        # adds new country objects to the list

    def addCountry(self):
        temp = False
        while temp == False:
            addCountry = input("What country would you like to add? ")
            if addCountry in self._cDictionary:         # if the country already exists
                print("Your country already exists. Try another.")
            else:
                temp = True
        addPopulation = int(input("What is the population of your country? "))
        addArea = float(input("What is the area of your country? "))
        addContinent = input("What continent is your country part of? ")
        callCountry = Country(addCountry,addPopulation,addArea,addContinent)
        self._catalogue.append(callCountry)
        self._cDictionary[addCountry] = addContinent

    def deleteCountry(self):
        self._countryName = input("What country would you like to delete? ")
        try:
            for i in self._catalogue:
                if i.getName() == self._countryName:        # if the country is in the list
                    self._catalogue.pop(self._catalogue.index(i))
            self._cDictionary.pop(self._countryName)
            print("Country deleted.")
        except:
            print("Couldn't delete country.")       # when country isn't in the list

    def findCountry(self):
        find = False
        while find == False:
            findCountry = input("What country would you like to find? ")
            if not findCountry in self._cDictionary:        # if country does not exist in the list
                print("Your country does not exist. Try another.")
            else:
                find = True
        for i in self._catalogue:
            if i.getName() == findCountry:          # printing out the country information
                print("Country:", i.getName())
                print("Area:", i.getArea())
                print("Popluation:", i.getPopulation())
                print("Population Density:", i.getPopDensity())
                print("Continent:", i.getContinent())

    def filterCountriesByContinent(self):
        byContinent = input("Enter a continent you want countries for: ")
        for i in self._cDictionary.items():
            if i[1] == byContinent:             # if the continent is in the list
                print(i[0])                     # printing out the countries that belong to the countries

    def printCountryCatalogue(self):
        print(self._catalogue)          # printing the catalogue

    def setPopulationOfASelectedCountry(self):
        askCountry = input("What country would you like to change the population for?: ")
        askPop = int(input("What is your country's new population?: "))
        for i in self._catalogue:
            if i.getName() == askCountry:           # if the country user input is in the name
                i.setPopulation(askPop)             # set the population to the user's input

    def findCountryWithLargestPop(self):
        largest = 0             # setting the number to lowest
        name = None             # name is blank
        for i in self._catalogue:       # looping to find the largest population
            if i.getPopulation() > largest:
                largest = i.getPopulation()
                name = i.getName()          # putting into a variable for print
        print(name + " has the largest population.")

    def findCountryWithSmallestArea(self):
        smallest = 10000000             # setting the number up high
        name = None         # name is blank
        for i in self._catalogue:
            if i.getArea() < smallest:      # loops to find the smallest area
                smallest = i.getArea()
                name = i.getName()          # putting it to a variable for print
        print(name + " has the smallest area.")

    def filterCountriesByPopDensity(self):
        lowbound = float(input("Enter the low bound for the population density range: "))       # user inputs low bound
        upperbound = float(input("Enter the upper bound for the population density range: "))   # user inputs upper bound
        for i in self._catalogue:
            if lowbound < i.getPopDensity() < upperbound:           # getting the countries with the population density between the user inputs
                print(i.getName())          # printing the country names

#    def findMostPopulousContinent(self):               Could not figure out how to do this one
#        continentsList = []
#        for (key,value) in self._cDictionary.items():
#            if value not in continentsList:
#                continentsList.append(value)
#        print(continentsList)
#        ss = continentsList
#        for k in range(len(continentsList)):
#            ss[k] = []
#            for i in range(len(self._catalogue)):
#                #print(self._catalogue[i].getContinent())
#                if self._catalogue[i].getContinent() == continentsList[k]:
#                    print(continentsList[k])
#                    ss[k].append[self._catalogue[i].getPopulation()]
#        print(ss)

    def saveCountryCatalogue(self, filename):
        self._out = open(filename, "w")
        self._list = []
        for i in sorted(self._cDictionary):
            self._list.append(i)
        for i in self._list:
            for k in self._catalogue:
                if i == k.getName():
                    self._list[self._list.index(i)] = k
        for i in self._list:
            self._out.write(i.getName() + "|" + i.getContinent() + "|" + str(i.getPopulation()) + "|" + str(i.getPopDensity()))
        self._out.close()
def main():
  cc = CountryCatalogue("data.txt")
  cc.saveCountryCatalogue("output.txt")


main()
