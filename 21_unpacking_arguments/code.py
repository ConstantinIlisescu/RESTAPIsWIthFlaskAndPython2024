# collect any given n umber of arguments in a tupple
def multiply(*args):
    print(args)
  
# use the * to destructure arguments in multiple parameters
multiply(1, 3, 5)

def add(x, y):
    return x + y

# you need to have the same number of items in the list as the number of arguments in the method
nums = [3, 5]
print(add(*nums))


nums_dict = {"x": 15, "y":25}
print(add(x=nums_dict["x"],y=nums_dict["y"]))
# simplified: take the method arguments and use them to grab the dictionary key if the same
print(add(**nums_dict))


def multiply_two(*args):
    total = 1
    for arg in args:
        total = total * arg
        
    return total


def apply(*args, operator):
    if operator == "*":
        return multiply(*args) # these will be a tuple so we need to add * at the start to unpack them back to an list
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."

    
print(apply(1, 2, 3, 4, operator="+" ))
