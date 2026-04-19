#Reverse a String
text = input("Enter string: ")
print(text[::-1])


#Check Palindrome
text = input("Enter text: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")



 #Find Largest Number in List


nums = [10, 25, 5, 40]

largest = nums[0]

for n in nums:
    if n > largest:
        largest = n

print("Largest:", largest)



#Count Vowels in String


text = input("Enter text: ")

count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Vowels:", count)

#Fibonacci Series


n = int(input("Enter number: "))

a, b = 0, 1

for i in range(n):
    print(a)
    a, b = b, a + b

#Intermediate Coding Questions

#Find Second Largest Number


nums = [10, 20, 5, 40]

nums.sort()

print("Second largest:", nums[-2])

#Remove Duplicates from List


nums = [1,2,2,3,4,4]

unique = list(set(nums))

print(unique)

#Check Prime Number



num = int(input("Enter number: "))

for i in range(2, num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")


#Count Words in Sentence


sentence = input("Enter sentence: ")

words = sentence.split()

print("Total words:", len(words))


#Find Common Elements in Two Lists


a = [1,2,3,4]
b = [3,4,5,6]

common = list(set(a) & set(b))

print(common)

#Advanced Beginner Interview Questions

#eck Armstrong Number


num = int(input())

order = len(str(num))
total = 0
temp = num

while temp > 0:
    digit = temp % 10
    total += digit ** order
    temp //= 10

if total == num:
    print("Armstrong")
else:
    print("Not Armstrong")

#Frequency of Characters


text = "programming"

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)


#Sort List Without Built-in

nums = [5,3,8,1]

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

print(nums)










#Star Pattern


for i in range(1,6):
    print("*" * i)


#Simple Password Validator

password = input("Enter password: ")

if len(password) >= 8:
    print("Strong password")
else:
    print("Weak password")


