# In Python dictionaries, keys can be of types like strings and integers,
#  but keep in mind that they can also be any other hashable types, such as tuples.

friend_ages = {
    "Rolf": 24,
    "Adam": 30,
}  # dictionaries have values, a value is a key value pair

# target a value using substring notation
friend_ages["Adam"]
friend_ages["Rolf"] = 20

friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 34},
]

print(friends[1]["name"])

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

# you can check if any keys are present in a dictionary, can't check for values, just key
if "Rolf" in student_attendance:
    print(f"Rolf: {student_attendance['Rolf']}")
else:
    print("Rolf is not a student of this class.")

# you can have only the values of a dictionary and calculate the average perhaps
attendance_values = student_attendance.values()
print(sum(attendance_values / len(attendance_values)))
