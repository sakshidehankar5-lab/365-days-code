#Create a Set 1
numbers = {1, 2, 3, 4, 5}
print(numbers)





#Add Element to Set 2
numbers = {1, 2, 3}
numbers.add(4)
print(numbers)





#Remove Element 3
numbers = {1, 2, 3, 4}
numbers.remove(2)
print(numbers)





#Union of Two Sets 4
a = {1, 2, 3}
b = {3, 4, 5}

result = a.union(b)
print(result)





#Intersection of Sets 5
a = {1, 2, 3}
b = {2, 3, 4}

print(a.intersection(b))




#Difference of Sets 6
a = {1, 2, 3}
b = {2, 3, 4}

print(a.difference(b))




#Check Membership 7
numbers = {10, 20, 30}

if 20 in numbers:
    print("Element exists")
else:
    print("Not found")


# Remove Duplicates from List 8

numbers = [1, 2, 2, 3, 4, 4, 5]

unique = set(numbers)
print(unique)





#Find Common Elements 9
list1 = {10, 20, 30}
list2 = {20, 40, 50}

common = list1 & list2
print(common)





#Count Unique Words 10
text = "python is easy and python is powerful"

words = text.split()
unique_words = set(words)

print(unique_words)
print("Total unique words:", len(unique_words))


