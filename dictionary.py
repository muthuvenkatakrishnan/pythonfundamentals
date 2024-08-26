names = {"name1" : "shriya" , "name2" : "Chetana" , "name3" : "spoorthi" , "name4" : "roopa"}
print(names["name1"])  #name1 is our key1 value

for item in names:
    print(item)  #it will print all the keys of the dictionary

for key in names:
    print(key)
    print(names[key])

names = {}
print(names)
