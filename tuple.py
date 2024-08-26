#creating a tuple:
empty_tuple = ()
single_element_tuple = (1,)
multi_element_tuple = (2,3,4,5)
mixed_tuple = (1,"hii" , 3.24, [1,2,3])

#acceess the elements of tuple
my_tuple = (10,20,30,40)
first = my_tuple[0] 
print(first)
print(my_tuple[1:3])   #for loop(start,stop) start to stop-1
print(my_tuple[-1])

#tuple operations

tuple1 = (1,2,3)
tuple2= (4,5,6)
print(tuple1+tuple2)

print(tuple1*2)

print(2 in tuple1)
print(9 in tuple1)

tuple3 = ()
tuple4 = tuple3 + (1,2,3)
print(tuple4)

#immutable in nature
#tuple4[0] = 10
#print(tuple4)   #type error

#tuple packing and unpacking
tuple5 = (1,2,3,"hello")   #packing
a,b,c,d,= tuple5
print(a)
print(b)   #unpacking
print(c)
print(d)

#nested tuples
tuple6 = (1,(2,3),(4,5),6)
print(tuple6[1])

#tuple methods
tuple7 = (1,2,4,2,6,5,8)  # this will return the number of times 2 is present
print(tuple7.count(2))

print(tuple7.index(6))  #it will return the index value of 6






