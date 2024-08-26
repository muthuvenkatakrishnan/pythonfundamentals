nums = [1,2,3,4,5,6,7,8]
#squares = [num * num for num in nums]  # list comprehension
#print(squares)

#for range(stop): 0 to stop-1
#squares = [num * num for num in range(9)]
#print(squares)

#range(start,stop) from start to stop-1
#squares = [num * num for num in range(1,9)]  #1 to 9-1
#print(squares)

#print the list of even numbers from 1 to 20 using list comprehension
evens = [num for num in range(1, 21) if num%2==0]
print(evens)


#list = ["apple" , "mango" , "banana" , "pine" , "grapes"]
#convert the fruits names into uppercase and print the new list with the fruits which is not having 'E' in it
list = ["apple" , "mango" , "banana" , "pine" , "grapes"]
list2 = [item.upper() for item in list if 'E' not in item.upper()]
print(list2)

#list of numbers which are completely divided by 2 and 3 from 1 to 50
div_by = [x for x in range(50) if x%2 == 0 and x%3 ==0]
print(div_by)
