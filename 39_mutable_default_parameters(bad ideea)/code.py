from typing import List, Optional

#Bad
class Student:
    def __init__(self, name:str, grades: List[int] = []): #This is bad
        self.name = name
        self.grades = grades
        
    def take_exam(self, result):
        self.grades.append(result)
        
        

bob = Student("Bog")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades) # this will print [90] as Bog take_exam asigned 90 to the list
print(rolf.grades) # this also prints [90] even if Rolf never took an exam, as the param is assigned to the same object in memory when defined at line #4




###Good 
class Student2:
    def __init__(self, name:str, grades: Optional[List[int]] = None): #This is good
        self.name = name
        self.grades = grades or [] # this is good
        
    def take_exam(self, result):
        self.grades.append(result)
        
        
bob2 = Student2("Bob2")
rolf2 = Student2("Rolf2")
bob2.take_exam(90)
print(bob2.grades) # this will print [90] as Bog2 take_exam asigned 90 to the list
print(rolf2.grades) # this will print [] as Rolf2 didn't take_exam 