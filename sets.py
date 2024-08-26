my_set = {1,2,3,4,56}
my_set.add(5)
print(my_set)

#remove an element
my_set.remove(3)
print(my_set)

#discard
my_set.discard(56)
print(my_set)

set = {1,2,3,4}  #since sets are unordered any index element can be popped
print(set.pop()) # it will print the elemnt that has been removed

#copy()

set1= {1,2,3,4}
set2= set1.copy()
print(set2)

#union
set3 = {2,3,4,5}
set4 = {3,4,7,8}
result = set3.union(set4)
print(result)

#intersection
result1 = set3.intersection(set4)
print(result1)

#difference
set5 = {1,2,3}
set6 = {2,3,4}
res = set6.difference(set5)  #elements present in set6 but not in set5
print(res)

#update()
set5.update(set6)  #similar to union()
print(set5)

#issubset()
my_set1 = {1,2}
my_set2 = {1,2,3,4}  #set1 is subbset of set2
#set2 is superset of set1
print(my_set1.issubset(my_set2))

#issuperset()
print(my_set2.issuperset(my_set1))

#isdisjoint()
my_set3 = {1,2,3}
my_set4 = {4,5,6}
print(my_set3.isdisjoint(my_set4))


