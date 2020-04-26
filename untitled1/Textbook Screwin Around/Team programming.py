characters = {}

file = open("Text", "w")
set1 = set(input("Type something").upper())
set2 = set(input("Type another thing").upper())

common = set1.intersection(set2)
file.write("The characters in both strings are:\n")
for alpha in sorted(common):
    print(alpha) 
