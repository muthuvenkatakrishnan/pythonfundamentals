for i in zip([1,2,3,4,5],["Rohan","Mohan","Charu Roopa","Spoorthi","Muthu"]):
    print(i)

mytup = (1,2,3,4,5)
print(mytup)

a,b,c,d,e = mytup
print(a,b,c,d,e)


for i in zip([1,2,3,4],['Apple','Orange','Banana','Kiwi'],['Autumn', 'Spring','Summer']):
    print(i)

from itertools import zip_longest
my_data = set(zip_longest([1,2,3,4],['Apple','Orange','Banana','Kiwi'],['Autumn', 'Spring','Summer','Winter']))
print(my_data)

my_zip = zip([1,2,3,4],['Apple','Orange','Banana','Kiwi'],['Autumn', 'Spring','Summer','Winter'])
nums, fruits, seasons = zip(*my_zip)
print("numbers: ",nums)
print("fruits: ",fruits)
print("Seasons: ",seasons)