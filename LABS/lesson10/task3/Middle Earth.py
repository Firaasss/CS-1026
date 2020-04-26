James Corbett, Firas Ab, Gavin Krohman, Vaishvik Patel

class Meppl:
    def __init__(self, n, y, l):
        self._name = n
        self._yearOfBirth = y
        self._location = l

    def __repr__(self):
        return self._name + " is from " + self._location

    def fightingStance(self, f):
        print("I can fight")

person = Meppl("Vaishvik", 1800, "London")
print(person)


