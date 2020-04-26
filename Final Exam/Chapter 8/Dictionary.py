countryInfo = dict()
for lines in open("data", "r").readlines():
    line = lines.split()
    name = line[1]
    income = line[2]
    countryInfo[name] = income
print(countryInfo)
