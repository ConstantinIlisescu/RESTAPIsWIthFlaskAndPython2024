def divide(divident, divisor):
    if divisor ==0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    
    return divident / divisor


grades = []

print("Welcome to the average grade program.")
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print("There are no grades yet in your list.")
else:
    ##this will only run if there is no except
    print(f"The average grade is {average}.")
finally:
    print("Thank you")