#1 Working with File Pointer
with open("example.txt", "r") as file:
    print(file.tell())   # Current position
    file.read(5)
    print(file.tell())   # Position after reading

    file.seek(0)         # Go back to beginning
    print(file.read(5))



#2. Handling Exceptions (Very Important)
try:
    with open("example.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File does not exist!")
except Exception as e:
    print("Error:", e)




#3. Writing Multiple Lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]

with open("example.txt", "w") as file:
    file.writelines(lines)





#4. Working with CSV Files
import csv

# Writing CSV
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 25])
    writer.writerow(["Bob", 30])

# Reading CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)




#5. Working with JSON Files
import json

data = {
    "name": "Alice",
    "age": 25
}

# Write JSON
with open("data.json", "w") as file:
    json.dump(data, file)

# Read JSON
with open("data.json", "r") as file:
    content = json.load(file)
    print(content)

#6. Rename and Delete Files
import os

os.rename("example.txt", "new_example.txt")  # Rename
os.remove("new_example.txt")                 # Delete

#7. Working with Directories
import os

os.mkdir("my_folder")        # Create folder
os.rmdir("my_folder")        # Remove empty folder
print(os.listdir())          # List files in directory




#18. Read & Write Both (`r+`, `w+`, `a+`)
with open("example.txt", "r+") as file:
    content = file.read()
    file.write("\nNew content added")



#9. File Handling with Encoding
with open("example.txt", "r", encoding="utf-8") as file:
    print(file.read())




#10. Mini Project: Word Count in File
with open("example.txt", "r") as file:
    text = file.read()
    words = text.split()
    print("Total words:", len(words))



#11. Mini Project: Count Lines, Words, Characters
with open("example.txt", "r") as file:
    content = file.read()

lines = content.split("\n")
words = content.split()

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", len(content))




#12. Copy Binary File (e.g., Image)
with open("image.jpg", "rb") as src:
    with open("copy.jpg", "wb") as dest:
        dest.write(src.read())



