openFile = open("split.txt", "r")
for lines in openFile:
    line = lines.rstrip()
    parts2 = line.split()
    print(parts2)

    #Bob, is a boy?
