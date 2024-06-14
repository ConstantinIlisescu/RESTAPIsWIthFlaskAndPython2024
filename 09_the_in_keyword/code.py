friends = ["Rolf", "Bob", "Jen"]
# can check if any value in list / sets / tuples or if a substring is in a string
print("Jen" in friends)  # true if in the list


# practice
movies_watched = {"The Matrix", "Green Book", "Her"}
user_movie = input("Enter something you've watched recently: ")

if user_movie in movies_watched:
    print(f"I've watched {user_movie} too!")
else:
    print("I haven't watched that yet.")

# magic app
number = 7
user_input = input("Enter 'y' if you would like to play: ")

if user_input in ("y", "Y"):
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1: # abs() returns the absolute number. i.e. for -1 the return is 1
        print("You were off by one.")
    else:
        print("Sorry, it's wrong!")
