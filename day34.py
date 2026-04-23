#for` Loop**
#Example: print numbers from 1 to 5
for i in range(1, 6):
    print(i)




#2.`while` Loop
# Example: print numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1




#*3.break` Statement**
# Example: stop when number is 3
for i in range(1, 6):
    if i == 3:
        break
    print(i)



#4. `continue` Statement**
# Example: skip number 3
for i in range(1, 6):
    if i == 3:
        continue
    print(i)




#5. `pass` Statement**
# Example: empty loop
for i in range(5):
    pass

print("Loop completed")
