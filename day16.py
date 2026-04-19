#armstrong number
num = int(input("Enter a number: "))

order = len(str(num))
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")




#print fibonacci series
n = int(input("Enter the number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c




#brute-force solution
l1 = [4,5,8,2,3,5]   # list of numbers ki list hai.
target = 10             #humein do numbers dhundhne hain jinka sum 10 ho.

for i in range(len(l1)):      #ek-ek karke select karta
    for j in range(i + 1, len(l1)):   #elements check karta hai.
        if l1[i] + l1[j] == target:    #do numbers ka sum check karta hai.
            print(l1[i], l1[j])         #10 ke barabar ho → pair print ho jata hai.
print(len(l1))




#check string "python is a SIP DOLLAR LANGUAGE" is a palindrome or not
s = "python is a SIP DOLLAR LANGUAGE"

# remove spaces and convert to lowercase
clean = s.replace(" ", "").lower()

if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")



#Python Program to Check Perfect Number
num = int(input("Enter a number: "))
sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i

if sum == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")


