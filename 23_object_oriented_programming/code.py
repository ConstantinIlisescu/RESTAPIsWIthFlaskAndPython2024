student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}

def average(sequence):
    return sum(sequence) / len(sequence)

print(average(student['grades']))


# rewrite the above as OOP

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
        
    def average_grade(self):
        return sum(self.grades) / len(self.grades)
        

student  = Student("Bob", (89, 90, 93, 78, 90))
print(student.name)
print(student.average_grade)

student_two  = Student("Rolf", (100, 90, 93, 98, 90))
print(student_two.name)
## this is what hapens under the hood
print(Student.average_grade(student_two))
