#write function taking two string arguments and returns:
# - a set consisting of the upper and lowercase letters that are contained in both strings
# - a set containing of upper and lowercase letters not in either string
# - a set consisting of all non-letter characters combined in both strings
x = set(input("String 1: "))
y = set(input("String 2: "))
uppercase = []
lowercase = []
nonLetters = []

def twoStrings(x, y):
    matches = x.intersection(y)
    for i in matches:
        if i.isupper():
            uppercase.append(i)
            print(uppercase)
        elif i.islower():
            lowercase.append(i)
            print(lowercase)
    for i in x.union(y):
        if i not in "abcdefghijklmnopqrstuvwxyz":
            print(i)
print(twoStrings(x, y))


