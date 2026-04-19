#Python Dictionary Basics
student = {
    "name": "Rahul",
    "age": 21,
    "course": "BCA"
}

#Access Values
print(student["name"])   # Rahul
print(student.get("age"))

# Add / Update Values
student["age"] = 22          # update
student["city"] = "Mumbai"   # add




#Remove Values
student.pop("course")

#Loop Through Dictionary
for key, value in student.items():
    print(key, value)




#Important Methods
student.keys()     # all keys
student.values()   # all values
student.items()    # key-value pairs

#Dictionary Example (Real Use)

#Example: Shopping Cart
cart = {
    "apple": 2,
    "banana": 5,
    "milk": 1
}

total_items = sum(cart.values())
print(total_items)




#Nested Dictionary
students = {
    "s1": {"name": "Rahul", "age": 21},
    "s2": {"name": "Amit", "age": 22}
}
print(students["s1"]["name"])


