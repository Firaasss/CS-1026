numPassing = 0
numFailing = 0

total = 0
count = 0

maxGrade = 0.0
minGrade = 100.0

grade = float(input("Enter a grade or -1 to finish: "))
while grade >= 0.0:
    if grade >= 50:
        numPassing = numPassing + 1
    else:
        numFailing = numFailing + 1

    if grade < minGrade:
        minGrade = grade
    if grade > maxGrade:
        maxGrade = grade

    grade = float(input("Enter another grade or -1 to end: "))

print("There are %.2d people passing" % numPassing)
print("There are %.2d people failing" % numFailing)
print("The highest grade is", maxGrade)
print("The minimum grade is", minGrade)



