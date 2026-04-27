#Create a Set
numbers = {1, 2, 3, 4, 5}
print(numbers)



#Create a Set from a List

my_list = [1, 2, 2, 3, 4, 4]
my_set = set(my_list)
print(my_set)



#Add an Element to a Set
fruits = {"apple", "banana", "mango"}
fruits.add("orange")
print(fruits)


# Remove an Element

colors = {"red", "blue", "green"}
colors.remove("blue")
print(colors)



# Union of Two Sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.union(set2)
print(result)



#Intersection of Two Sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.intersection(B))

#Difference Between Sets
A = {1, 2, 3, 4}
B = {3, 4}

print(A.difference(B))

#Check if Element Exists

numbers = {10, 20, 30, 40}

if 20 in numbers:
    print("20 is in the set")


# Remove Duplicate Elements

data = [1, 1, 2, 3, 3, 4, 5]
unique_data = set(data)

print(unique_data)

# Loop Through a Set
animals = {"cat", "dog", "lion"}

for animal in animals:
    print(animal)

