def named(**kwargs):
    print(kwargs)
    
# the key word arguments gets colected and put in a dictionary
named(name="bob", age=25) 
# prints {"name": "bob", "age": 25}


###########################################
def named_two(name, age):
    print(name, age)
    
details = {"name": "Bob", "age": 25}

# unpack the dictionary into two named arguments
named_two(**details)
named(**details)

###########################################
def both(*args, **kwargs):
    print(args)
    print(kwargs)
    
    
both(1, 3, 5, name="Bob", age="25")