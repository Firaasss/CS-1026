# Replace the placeholders with code and run the Python program

class Dinosaur:
    def __init__(self):
        self._type = type

    def setType(self, type):
        self._type = type

    def getType(self):
        return self._type

# Create three dinsosaurs
d1 = Dinosaur()
d2 = Dinosaur()
d3 = Dinosaur()

# Set their types
d1.setType("T-Rex")
d2.setType("Velociraptor")
d3.setType("Stegosaurus")

# Print the types
print(d1.getType())
print(d2.getType())
print(d3.getType())
