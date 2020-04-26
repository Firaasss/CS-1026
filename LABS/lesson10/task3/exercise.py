class Car:
    def __init__(self, efficiency, fuel = 0):
        self._efficiency = efficiency
        self._fuel = fuel

    def drive(self, distance):
        self._distance = distance

    def addGas(self, amount):
        self._gas = self._fuel + amount

    def getGasLevel(self):
        return (self._gas - self._distance / self._efficiency)

myHybrid = Car(50)
myHybrid.addGas(20)
myHybrid.drive(100)
print(myHybrid.getGasLevel())
