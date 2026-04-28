#1. Using `and`
age = 20
has_license = True

if age >= 18 and has_license:
    print("You can drive")
else:
    print("You cannot drive")



#2. Using `or`
marks = 35

if marks >= 40 or marks == 35:
    print("You passed")
else:
    print("You failed")



#3. Using `not`
is_raining = False

if not is_raining:
    print("Go outside")
else:
    print("Stay inside")



#4. Combining `and` + `or`
age = 25
income = 30000

if age > 18 and (income > 25000 or age > 30):
    print("Loan approved")
else:
    print("Loan rejected")



#5. Login System Example
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")




#6. Even Number Check using `not`
num = 7

if not (num % 2 == 0):
    print("Number is odd")
else:
    print("Number is even")


#7. Range Check
num = 15

if num >= 10 and num <= 20:
    print("Number is between 10 and 20")
else:
    print("Out of range")
