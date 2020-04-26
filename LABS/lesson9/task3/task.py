# Replace the placeholders with code and run the Python program

sentence ="I had such a horrible day. It was awful, so bad, sigh. It could not have been worse but actually though "\
          +"such a terrible horrible awful bad day."

makeItHappy ={"horrible":"amazing","bad":"good","awful":"awesome","worse":"better","terrible":"great"}

newSentence = sentence.split()
for word in newSentence:
    if word in makeItHappy:
        word = word.replace(word, makeItHappy[word])

newString=""

for word in newSentence:
    newString = newString + word + " "

print(newString)

