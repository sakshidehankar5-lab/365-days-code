#list,set,tuple,dictionary


list1=[1,"python","ram",215]
print(type(list1))
print(list1)


#sclicing
list1=[1,"python","ram",215]
print(type(list1))
print(list1[3:])
#output: [215]


#sclicing
list1=[1,"python","ram",215]
print(type(list1))
print(list1[0:2])
#output: [1,python]



#user se input leke
list1=[]
n=int(input("enter the number of element :"))

for i in range(0,n):
    ele=int(input())
    list1.append(ele)

print(list1)




#dictionary
d={1:'abc',2:'skh',3:'xyz'}
print(d)

#assesing value using keys
print("1st name is "+d[1])
print("2nd name is "+d[3])

print(d.keys())
print(d.values())