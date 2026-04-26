#1. Convert Celsius to Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit:", fahrenheit)






#2. Convert Kilometers to Miles
km = float(input("Enter distance in kilometers: "))

miles = km * 0.621371

print("Distance in miles:", miles)








#3. Swap Two Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)





## 4. Find the Largest of Three Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

largest = max(a, b, c)

print("Largest number is:", largest)






#5. Check Even or Odd Number
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")




#6. Calculate Simple Interest
p = float(input("Enter Principal amount: "))
r = float(input("Enter Rate of interest: "))
t = float(input("Enter Time (years): "))

si = (p * r * t) / 100

print("Simple Interest:", si)
