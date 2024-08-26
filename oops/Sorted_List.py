def sorted_list(n):
    return n[-1]

def sort_by_last(tuples):
    return sorted(tuples,key=sorted_list)

my_sorted_list = sort_by_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
print(my_sorted_list)

# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

my_lst = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
for i in range(len(my_lst)):
    if i not in [0,4,5]:
        print(my_lst[i])

# 17. Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
# Sample Data:
# ([0, 3, 4, 7, 9]) -> False
# ([3, 5, 7, 13]) -> True
# ([1, 5, 3]) -> False

def isPrime(n):
    factor = 0
    for i in range  (1,n+1):
        if n%i == 0:
            factor += 1
    
    if factor == 2:
        return True
    else:
        return False

def prime_check(my_list):
    return all (isPrime(i) for i in my_list)

lst1 = [0, 3, 4, 7, 9]
lst2 = [3, 5, 7, 13]
result = prime_check(lst1)
result2 = prime_check(lst2)
print(f"{lst1}: -> {result}")
print(f"{lst2}: -> {result2}")

# 18. Write a Python program to generate all permutations of a list in Python.

