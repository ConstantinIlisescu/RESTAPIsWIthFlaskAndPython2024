def add(x, y):  # values passed to the function when created called parameters
    result = x + y
    print(result)

add(5, 3)  # values passed to the function when called, are arguments

def say_hello(name, surname):
    print(f"Hello, {name} {surname}")
# named or key word arguments
say_hello(surname="Bob", name="Smith")
