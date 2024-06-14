def add(x, y):
    print(x + y)


add(5, 8)  # will print 13
result = add(5, 8)  # will print 13

# will print None (special value in python that means no value or undeclared value)
# functions by default returns None if no return value is defined
print(result)


def add_and_return(x, y):
    return x + y


print(add_and_return(5, 8))
