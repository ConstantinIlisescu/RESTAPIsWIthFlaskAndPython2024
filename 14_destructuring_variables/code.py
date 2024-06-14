# deconstruct tuples
x, y = 5, 11

t = 1, 2
x, y = t

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

person = ("Bob", 42, "Mechanic")
# _ is convention name for variables that want to be ignored
name, _, profession = person

my_list = [1, 2, 3, 4, 5]
# deconstruct first and second value then collect all the remaining ones in a variable,
a, b, *c = my_list
# you can also collect any values from any index range
a, *b, c = my_list
print(a)
print(b)
print(c)
