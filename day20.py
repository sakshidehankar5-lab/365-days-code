# 1. Print Numbers from 1 to 10 (for loop)
for i in range(1, 11):
    print(i)


#2. Print Even Numbers from 1 to 20
for i in range(1, 21):
    if i % 2 == 0:
        print(i)



# 3. Sum of Numbers from 1 to n
n = int(input("Enter a number: "))
sum = 0

for i in range(1, n+1):
    sum += i

print("Sum =", sum)



## 4. Multiplication Table
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num*i)



## 5. Factorial of a Number
num = int(input("Enter a number: "))
fact = 1

for i in range(1, num+1):
    fact *= i

print("Factorial =", fact)




## 6. Print Numbers using while loop
i = 1

while i <= 10:
    print(i)
    i += 1




## 7. Reverse a Number
num = int(input("Enter number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print("Reversed number:", rev)




## 8. Star Pattern
rows = 5

for i in range(1, rows+1):
    print("*" * i)


