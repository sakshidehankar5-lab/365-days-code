#Create a tuple
t = (1, 2, 3)
print(t)





#Access elements
t = (10, 20, 30)
print(t[0])   # first element
print(t[2])   # last element




#Tuple unpacking
t = (5, 10)
a, b = t

print(a)
print(b)




#Loop through a tuple
t = (1, 2, 3, 4)

for i in t:
    print(i)




#Single element tuple
t = (5,)
print(type(t))





#Tuple methods
t = (1, 2, 3, 1, 1)

print(t.count(1))   # how many times 1 appears
print(t.index(2))   # index of 2





#Nested tuple
t = ((1, 2), (3, 4))

print(t[0])
print(t[1][1])

#Tuple cannot be changed (immutable)
