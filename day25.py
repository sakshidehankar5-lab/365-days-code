# Exception Handling in Python
#1Basic Syntax
try:
    # Code that may cause an exception
    x = int(input("Enter a number: "))
    print(10 / x)

except ZeroDivisionError:
    print("Cannot divide by zero!")

except ValueError:
    print("Invalid input! Please enter a number.")






#2 Using a General Exception
try:
    x = int(input("Enter a number: "))
    print(10 / x)

except Exception as e:
    print("Error occurred:", e)







#3 Using `else` and `finally`
try:
    x = int(input("Enter a number: "))
    result = 10 / x

except ZeroDivisionError:
    print("Cannot divide by zero!")

else:
    print("Result is:", result)

finally:
    print("Execution completed.")











#4 Raising Exceptions Manually
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above")
    return "Eligible"

try:
    print(check_age(16))
except ValueError as e:
    print(e)





#5 Custom Exception
class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error")
except CustomError as e:
    print(e)
