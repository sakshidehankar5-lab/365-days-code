#1Create and Write to a File
file = open("example.txt", "w")
file.write("Hello, this is Python file handling.")
file.close()





#2Read a File
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()




#3Append Data to File
file = open("example.txt", "a")
file.write("\nThis line is added later.")
file.close()




#4Read File Line by Line
file = open("example.txt", "r")
for line in file:
    print(line)
file.close()




#5Count Words in File
file = open("example.txt", "r")
text = file.read()
words = text.split()
print("Total words:", len(words))
file.close()



#6Count Lines in File
file = open("example.txt", "r")
lines = file.readlines()
print("Total lines:", len(lines))
file.close()




#7Using `with` (Best Method)
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
