###



numberGrades = int(input("How many student grades are there? "))
total = 0
for i in range(numberGrades):
    studentGrade = int(input("Please enter a grade"))
    total = total + studentGrade

avgGrade = total / numberGrades
print("The average score of the student grades is %",avgGrade,)


