alphabet = set("abcdefghijklmnopqrstuvwxyz")
setWords = set()
dictWords = {}
for i in open("Vik", "r").readlines():
    words = i.split()
    for word in words:
        word = word.lower()
        setWords.add(word)
for i in sorted(alphabet):
    for item in setWords:
        if i in item:
            dictWords[i] = item
print(dictWords)
            #print("Letter: ", i , "Word: ", item)
