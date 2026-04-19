#Prime Number Check
num = int(input("Enter a number: "))
flag = 0

for i in range(2, num):
    if num % i == 0:
        flag = 1
        break

if flag == 0:
    print("Prime Number")
else:
    print("Not a Prime Number")










#Fibonacci Series
n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c







#Reverse a Number
num = int(input("Enter number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reverse =", rev)







#palindrome number check
num = int(input("Enter number: "))
temp = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")













#lagest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Largest =", a)
elif b > c:
    print("Largest =", b)
else:
    print("Largest =", c)














#matliplication table
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)dat