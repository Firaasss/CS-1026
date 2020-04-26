import random

randomNumbers = []
while len(randomNumbers) < 20:
    randomNumbers.append(random.randint(0, 100))

print(randomNumbers)
randomNumbers.sort()
print("sorted:", randomNumbers)
