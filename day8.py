#Student marks program:
student_marks = {
    "Rahul": 85,
    "Amit": 90,
    "Priya": 78,
    "Neha": 92
}

name = input("Enter student name: ")

if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found")