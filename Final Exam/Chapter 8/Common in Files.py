firas = set()
vik = set()

for i in open("Firas", "r").readlines():
    words = i.split()
    print(words)
    for word in words:
        firas.add(word)
for i in open("Vik", "r").readlines():
    words = i.split()
    for word in words:
        vik.add(word)

#print(sorted(firas.intersection(vik)))

