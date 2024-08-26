# Deep Copy:
# Creates a new object 
# It is going to copy the contents of the original object into the new object
# The actual object content will remain unchanged

# Understanding how shallow copy works:

a = [1,2,3,4,5]
b = a
print(f"A list: {a}")
print(f"B list: {b}")
b.remove(3)

print(f"A list: {a}")
print(f"B list: {b}")

# In the above example the changes will affect both the objects. 
# Understanding how deep copy works


import copy
my_lst = [1,2,3,4,5,6]
your_list = copy.deepcopy(my_lst)

print(f"My List: {my_lst}")
print(f"Your List: {your_list}")

your_list.remove(5)

print(f"My List: {my_lst}")
print(f"Your List: {your_list}")
