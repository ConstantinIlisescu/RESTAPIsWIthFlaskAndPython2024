# default parameters needs to go after the positional arguments were defined if any
# not recommended to use variable to define the optional default properties
#       as the function will replace the variable with the actual value at runtime and will
#       not modified it if the variable is reassigned another value
default_y = 10


def add(x, y=default_y):
    print(x + y)


add(5)  # print 15

default_y = 3

add(5)  # also prints 15
