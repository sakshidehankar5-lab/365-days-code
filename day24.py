#Simple Generator Example
def count_up_to(n):
    i = 1
    while i <=n:
        yield i
        i += 1

for num in count_up_to(5):
    print(num)




#Generator with List-like behavior
def square_numbers(n):
    for i in range(n):
        yield i * i

gen = square_numbers(5)

print(next(gen))
print(next(gen))
print(next(gen))



#Generator Expression
squares = (x*x for x in range(5))

for i in squares:
    print(i)
