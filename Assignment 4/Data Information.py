file = open("data.txt", "r",encoding="utf-8")
readCountries = file.readlines()[1:]
for line in readCountries:
    dataCountries = line.rstrip("\n")
    stripCountries = dataCountries.split("|")
    pop = int(stripCountries[1].replace(',', ''))
    area = float(("%.2f" % (stripCountries[2].replace(',', '').replace('.', ''))))
    name = stripCountries[0]
    print(area)
