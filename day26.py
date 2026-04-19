
#2. Reading a File
file = open("example.txt", "r")
data = file.read()
print(data)
file.close()






#Read line by line
file = open("example.txt", "r")
for line in file:
    print(line)
file.close()







#Read one line
file = open("example.txt", "r")
print(file.readline())
file.close()











#3. Writing to a File
#Write (overwrites)
file = open("example.txt", "w")
file.write("Hello World")
file.close()






#Append
file = open("example.txt", "a")
file.write("\nNew line added")
file.close()






#4 Using `with` (Best Practice)

#Automatically closes file (no need for `close()`)
with open("example.txt", "r") as file:
    data = file.read()
    print(data)








#5. Writing with `with`
with open("example.txt", "w") as file:
    file.write("Python is easy!")




#6. File Exists Check
import os

if os.path.exists("example.txt"):
    print("File exists")
else:
    print("File not found")



#7. Deleting a File
import os

if os.path.exists("example.txt"):
    os.remove("example.txt")

#8. Working with Binary Files
with open("image.jpg", "rb") as file:
    data = file.read()




#9. Simple Example Program
# Write to file
with open("data.txt", "w") as f:
    f.write("Name: Rahul\nAge: 20")

# Read from file
with open("data.txt", "r") as f:
    print(f.read())


