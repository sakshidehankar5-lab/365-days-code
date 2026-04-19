#1st program (sorted)
s=[2,6,3,2,6]
r=set(s)
print(s)
print(sorted(r))


#2nd program (lick code)
a=[3,4,5,6,3]
target = 9
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==target:
            print(a[i],a[j])


#3 program
A="Alphabetical"
op=""
for ch in A:
    if ch not in op:
        op+=ch
print(op)



#4th program
s1=[3,4,7]
s2=[3,4,6]

if s1==s2:
    print("list hsve same elements")
else:
    print("list have different elements")



#5th program
s1=[3,4,5]
s2=[2,3,4,5,6,7]
if set(s1).issubset(set(s2)):
    print("s1 elements are included in s2")
else:
    print("s1 elements are not include in s2")



#6th program
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="")
    print("")

