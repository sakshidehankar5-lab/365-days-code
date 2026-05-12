#Fibonacci Series
n = int(input("How many terms? "))
a, b = 0, 1

for _ in range(n):
    print(a)
    a, b = b, a + b



Simple Student Grade System
name = input("Enter student name: ")
marks = float(input("Enter marks: "))

if marks >= 90:
    grade = "A"

elif marks >= 75:
    grade = "B"

elif marks >= 50:
    grade = "C"

else:
    grade = "Fail"

print(f"{name} got grade {grade}")
