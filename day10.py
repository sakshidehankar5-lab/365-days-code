#star patterns programs
#1st program
rows = 5
cols = 5
for i in range(rows):
    print("*" * cols)





#2nd program
#check whether is armstrong (or , not)
n = int(input("Enter number: "))
s = 0
temp = n
p = len(str(n))

while temp > 0:
    d = temp % 10
    s = s + d**p
    temp = temp // 10

if s == n:
    print("Armstrong number")
else:
    print("Not Armstrong number")




#3rd program
n=1251
power=len(str(n))
total=0
temp=n
while temp>0:
    rem=temp % 10
    total= total + rem ** power
    temp = temp //10
    print(total)





#4th program
for i in range(5):
    for j in range(5):
        print("*" * cols)





#5th program
for i in range(5):
    for j in range(5):
        print("*")





#6th program(1st way)
for i in range(1,6):
    print("*" * i)




#7th program(2nd way)
i=1
while i <=5:
    print("*" * i)
    i += 1





#8th program(1st way)
for i in range(5,0,-1):
    print("*" * i)




#9th program(2nd way)
i=5
while i >=1:
    print("*" * i)
    i -= 1




#10th program(1st way)
for i in range(3):
    print("******")




#11th program
#pyramid
rows = 5
for i in range(1,rows +1):
    print(" " *(rows-i)+ "*" *(2 * i-1))




#12th program
#pyramid
for i in range(6):
    for m in range(5-i):
        print("",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()
for i in range(5,0,-1):
    for j in range(5-i):
        print("",end="")
    for s in range(2*i-1):
        print("*",end="")
    print()


