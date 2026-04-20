#1. String Creation
#A string is a sequence of characters enclosed in quotes.
# Single quotes
s1 = 'Hello'


# Double quotes
s2 = "World"


# Triple quotes (multi-line)
s3 = '''This is
a multi-line
string'''

# Using str() constructor
s4 = str(123)  # "123"





#2. String Indexing
s = "Python"

print(s[0])   # P
print(s[1])   # y

# Negative indexing (from end)
print(s[-1])  # n
print(s[-2])  # o





#3. String Slicing
s = "Python"
print(s[0:4])   # Pyth
print(s[:3])    # Pyt
print(s[3:])    # hon
print(s[-3:])   # hon

# Step slicing
print(s[::2])   # Pto
print(s[::-1])  # nohtyP (reverse)




#4. String Methods
#Common built-in methods:
s = "hello world"

print(s.upper())        # HELLO WORLD
print(s.lower())        # hello world
print(s.capitalize())   # Hello world
print(s.title())        # Hello World

print(s.strip())        # removes spaces
print(s.replace("world", "Python"))  # hello Python

print(s.split())        # ['hello', 'world']
print("-".join(['a','b','c']))  # a-b-c

print(s.find("world"))  # index of word
print(s.count("l"))     # count occurrences

print(s.startswith("he"))  # True
print(s.endswith("ld"))    # True




#Complete Example Program
name = "John"
course = "Python Programming"

# Creation
text = f"{name} is learning {course}"

# Indexing
print(text[0])     # J

# Slicing
print(text[0:4])   # John

# Methods
print(text.upper())
print(text.replace("John", "Alice"))

# Formatting
age = 22
print(f"{name} is {age} years old")
