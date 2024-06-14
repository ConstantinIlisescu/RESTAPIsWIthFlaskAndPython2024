numbers = [1, 3, 5]
doubled = [x * 2 for x in numbers]

# from this
for num in numbers:
    doubled.append(num * 2)
# to this
[num * 2 for num in numbers]


friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_with_s = [x for x in friends if x.startswith("S")]

# from this
for friend in friends:
    if friend.startswith("S"):
        starts_with_s.append(friend)
# to this
[friend for friend in friends if friend.startswith("S")]
