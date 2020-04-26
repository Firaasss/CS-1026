# Implement a class Address. An address has a house number, a street, an optional
#apartment number, a city, a state, and a postal code. Defne the constructor such that
#an object can be created in one of two ways: with an apartment number or without.
#Supply a print method that prints the address with the street on one line and the city,
#state, and postal code on the next line. Supply a method def comesBefore(self, other)
#that tests whether this address comes before other when compared by postal code

class Address:
    def __init__(self, house, street, apt, c, s, p):
        self._house = int(house)
        self._street = street
        self._aptNumber = int(apt)
        self._city = c
        self._state = s
        self._postal = p

    def getApt(self):
        return self._aptNumber

    def getHouse(self):
        return self._house

    def getStreet(self):
        return self._street

    def getCity(self):
        return self._city

    def getState(self):
        return self._state

    def getPostal(self):
        return self._postal

    def __repr__(self):
        return "The address is", int(self._house), ",", str(self._street), "\n in", str(self._city), ",", str(self._state), ",", str(self._postal)

print(Address(810, "Wildrose Lane", 4, "London", "Ontario", "N6H5X5"))


