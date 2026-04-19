# 1.Basic lambda
add = lambda a, b: a + b
print(add(3, 5))   # Output: 8



#2. Square of a number
square = lambda x: x * x
print(square(4))   # Output: 



#3. With multiple argument
multiply = lambda x, y, z: x * y * z
print(multiply(2, 3, 4))   # Output: 24



#1. With `map()`
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)   # [1, 4, 9, 16]


#2. With `filter()
nums = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)   # [2, 4]

#With `sorted()
pairs = [(1, 3), (2, 1), (4, 2)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)   # [(2, 1), (4, 2), (1, 3)]


#Using `def`
def add(a, b):
    return a + b


#Inline `if-else` example
check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(5))   # Odd
