def add(x, y):
    return x + y


# equivalent as lambda function
add = lambda x, y: x + y


def double(x):
    return x * 2


sequence = [1, 3, 5, 9]
double = [double(x) for x in sequence]  # list comprehensions
# this is useful if you want to have similarities if working with developers coming from other programming languages like JS
double = list(map(lambda x: x * 2, sequence))
