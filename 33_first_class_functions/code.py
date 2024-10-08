def divide(divident, divisor):
    if divisor == 0:
        raise ZeroDivisionError('Divisor cannot be 0.')
    
    return divident / divisor

def calculate (*values, operator):
    return operator(*values)

result = calculate(20, 6, operator=divide)

print(result)

#########################################################

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}")

friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Ane", "age": 27}
]

def get_friend_name(friend):
    return friend['name']

print(search(friends, "Rolf", get_friend_name))

## using lambda
print(search(friends, "Rolf", lambda friend: friend['name']))