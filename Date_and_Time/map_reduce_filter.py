# normal way
my_num = [2,4,5]
result = []
for i in my_num:
    result.append(i**3)

print(result)

# Using list comprehension
result = [i**3 for i in my_num]
print(result)

# Using lambda expression
result = lambda my_num: [i**3 for i in my_num]
print(result(my_num))

# Using map function
def cube(n):
    return n ** 3

result = map(cube,my_num)
print(list(result))

# to make use of reduce function we need to import functools
# import functools

from functools import reduce as red
my_lst = [1,2,3,4,5]
product = red(lambda a,b: a*b,my_lst)
print("5 Factorial is: ", product) 


def is_prime(n):
    factor = 0
    for i in range (1,n+1):
        factor += 1 if n%i == 0 else 0
    return factor == 2

my_lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
prime_list = filter(is_prime,my_lst)
print("Prime number list: ", list(prime_list))