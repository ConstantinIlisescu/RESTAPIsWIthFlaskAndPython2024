users = [
    (0, "Bob", "password"),
    (1, "Relf", "bob123"),
    (2, "Jose", "longp4assword"),
    (3, "username", "1234"),
]

# dictionary comprehensions
username_mapping = {user[1]: user for user in users}

username_input = input("Enter your username: ")
password_input = input("Enter your passord: ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("Your details are correct!")
else:
    print("Your details are incorect.")