#1st program
#palindrome
sentence = "python is a interpreted language"
# Step 1: Remove spaces
no_space = sentence.replace(" ", "")
reversed_sentence = no_space[::-1]                          #Reverse the string
if no_space.lower() == reversed_sentence.lower():           #Check palindrome
    print("It is a palindrome")
else:
    print("Not a palindrome")

#2st program
#max and min
#a=int(input("enter any number"))
nums = [8, 2, 7, 5]
print("Minimum:", min(nums))
print("Maximum:", max(nums))



#3rd program
#using max and min (show indexing value)
nums = [8, 2, 7, 5]
nums.sort()
print("Second largest:", nums[-2])


#4th program
l=[2,6,8,9,3,2,6]
l=list(set(l))
l.sort()
print(l[-2])


#5th program
text = input("Enter: ")
freq = {}
for ch in text:
    if ch != " ":
        freq[ch] = freq.get(ch, 0) + 1
print(freq)



#6th program
s="programing"
freq = {}
for ch in s:
        freq[ch] = freq.get(ch,0) + 1
print(freq)



#7th program
#using max and min (show indexing value)
nums = [8, 2, 7, 5]
nums.sort()
print("Second smallest:", nums[1])



#8th program
a=[2,5,2,7,5]
b=[3,5,3,6]
result = list(set(a) & set(b))      # Convert lists to sets and use &

print(result)
