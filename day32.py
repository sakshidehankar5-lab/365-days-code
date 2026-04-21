# -------------------------------
# 1. Creating Tuples
# -------------------------------
t1 = (1, 2, 3)
t2 = "a", "b", "c"        # packing
t3 = (5,)                 # single element tuple
t4 = tuple([10, 20, 30])  # from list

print("Tuples:")
print(t1)
print(t2)
print(t3)
print(t4)

# -------------------------------
# 2. Tuple Operations
# -------------------------------
t = (10, 20, 30, 40)

print("\nAccessing elements:")
print(t[0])      # first element
print(t[-1])     # last element

print("\nSlicing:")
print(t[1:3])    # elements from index 1 to 2

print("\nConcatenation:")
t_new = t1 + t4
print(t_new)

print("\nRepetition:")
print((1, 2) * 3)

print("\nMembership:")
print(20 in t)

print("\nLength:")
print(len(t))

# -------------------------------
# 3. Tuple Unpacking
# -------------------------------
print("\nUnpacking:")
t5 = (1, 2, 3)
a, b, c = t5
print(a, b, c)

print("\nExtended Unpacking:")
t6 = (1, 2, 3, 4, 5)
x, *y = t6
print("x =", x)
print("y =", y)

# Swapping variables
print("\nSwapping:")
a = 5
b = 10
a, b = b, a
print("a =", a, "b =", b)

# -------------------------------
# 4. Tuple vs List
# -------------------------------
print("\nList vs Tuple:")

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

# List is mutable
my_list[0] = 100
print("Modified list:", my_list)

# Tuple is immutable
# my_tuple[0] = 100  # This will cause an error

print("Tuple (unchanged):", my_tuple)

# Tuple methods
print("\nTuple methods:")
t7 = (1, 2, 2, 3)
print("Count of 2:", t7.count(2))
print("Index of 3:", t7.index(3))