#constructor is the def function within the class and all the contents that go with it
#What class is the class MAnager a sub class of? Employee
#What class is the class Executive a subclass of? Manager
#If you create an object of the class, what instance variables would it have? self._manager/self._salary/self._department

#What does super() do in the class Manager? You're referencing the superclass
#Write a method for the class Manager that will get the department name of a manager:
def getDept(self):
    return self._department


#create main method that will create Manager object for "Mickey Mouse" who managers "entertainment department"
#Has salary of $83k. Create object for "Walt Disney" who is the executive for the entertainment department w/ salary $195k.
#print each object

def main():
    aMain = Manager("Mickey Mouse", 83000, "Entertainment")
    Executive = Executive("Walt Disney", 195000, "Entertainment")
    print(aMain)
    print(Executive)

main()

#create class Executive Assistant for employees working as assistant to executive in company. Include name of exec they work for.

class ExecAssistant:
    def__init__(self, nP, nE)
        self._name = nP
        self._nameofExec = nE
    def getNameOfExec(self):
        return self._nameOfExec

    def setSalary(self, s):
        self._salary = s
