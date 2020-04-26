class Country:
    def __init__(self, name, pop, area, continent) :
       self._name = str(name)
       self._pop = int(pop)
       self._area = float(area)
       self._continent= str(continent)
    def setPopulation(self, pop):
        self._pop = pop
    def getName(self):
        return self._name
    def getPopulation(self):
        return self._pop
    def getArea(self):
        return self._area
    def getContinent(self):
        return self._continent
    def getPopDensity(self):
       return self._pop/self._area
    def __repr__(self):
        return self._name + "is in" + self._continent + "with a population density" + str(self.getPopDensity())
class CountryCatalogue:
    def __init__(self, filename):
        self._cDictionary = {}
        self._catalogue = set()
        file = open("data", "r")
        for line in file:
            data = line.rstrip("\n")
            dataStrip = data.split("|")
            population = int(dataStrip[1].replace(',', ''))
            area = float(dataStrip[2].replace(',', '').replace('.', ''))
        for line in file:
            data = line.rstrip("\n")
            dataStrip = data.split("|")
            self._catalogue.add(dataStrip[0])
        file2 = open("continent","r")
        for line in file2:
            data2 = line.rstrip("\n")
            dataStrip2 = data2.split(",")
            country = dataStrip2[0]
            continent = dataStrip2[1]
            self._cDictionary[country] = continent
    def addCountry(self):
        enterCountry = input("please enter a country")
        enterPopulaiton = input("please enter population of the country")
        enterArea = input('please enter area of the country')
        enterContinent = input('please enter continent of the country')
        while True:
            enterCountry = input('Please enter a country')
            if enterCountry in self._catalogue:
                print('sorry, the country entered is already present in the list')
            else:
                self._catalogue.add(enterCountry)
                self._cDictionary[enterCountry] = enterContinent
                break
    def deleteCountry(self):
        enterCountry = input("please enter a country")
        if enterCountry in self._catalogue:
            self._catalogue.remove(enterCountry)   #remove doesnt work.
    def findCountry(self):
        enterCountry = input("please enter a country")
        if enterCountry in self._catalogue:
            print(self._catalogue)
        else:
            print('This country does not exists in the catalogue')
    def filterCountriesByContinent(self):
        enterContinent = input('please enter a continent')
        if

    # def printCountryCatalogue(self):
    #
    # def setPopulationOfASelectedCountry(self):
    #
    # def findCountryWithLargestPop(self):
    #
    # def findCountryWithSmallestArea(self):
    #
    # def filterCountriesByPopDensity(self):
    #
    # def findMostPopulousContinent(self):
    #
    # def saveCountryCatalogue(self, filename):








