class Instructor:
    def __init__(self, n, yob, s, f):
        super().__init__(n, yob)
        self._name = n
        self.salary = s
        self._faculty = f
        self._courses = []

    def addCourse(self, a):
        self._courses.append(a)

    def __repr__(self):
        return self._name + " teaches in the faculty of " + self._faculty

f1 = Instructor("Albert Einstein", 1896, 40404943, "Physics")
print(f1)
