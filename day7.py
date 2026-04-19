# Dictionary in Python
# A dictionary is a collection of key-value pairs. It is unordered mutable, and indexed. Each key must be unique and immutable (like strings, numbers, or tuples), while the values can be of any data type.

student = {
    "name": "Rahul",
    "age": 20,
    "course": "BCA"
}
print(student)



# Nested dictionary
students = {
    "s1": {"name": "Rahul", "age": 20},
    "s2": {"name": "Amit", "age": 22}
}
print(students["s1"]["name"])




#Counting with dictionary
text = "apple banana apple"
words = text.split()

count = {}
for word in words:
    count[word] = count.get(word, 0) + 1

print(count)




#Sorting a dictionary
marks = {"Rahul": 80, "Amit": 90, "Neha": 85}

sorted_marks = dict(sorted(marks.items()))
print(sorted_marks)