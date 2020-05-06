class Student:
    def __init__(self, name, school, mark):
        self.name = name
        self.school = school
        self.mark = []


    def average(self):
        return sum(self.mark)/len(self.mark)

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary


rolf = WorkingStudent('Rolf', 'MIT', 15.50)
