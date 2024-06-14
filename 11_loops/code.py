# while loop
number = 7
while True:
    user_input = input("Would you like to play? (Y/n): ")

    if user_input == "n":
        break

    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif (
        abs(number - user_number) == 1
    ):  # abs() returns the absolute number. i.e. for -1 the return is 1
        print("You were off by one.")
    else:
        print("Sorry, it's wrong!")

    user_input = input("Would you like to play? (Y/n): ")


# for loop
friends = ["Rolf", "Jen", "Bob", "Anne"]

for friend in friends:
    print(f"{friend} is my friend.")


for friend in range(len(friends)):
    print(f"{friend} is my friend.")
