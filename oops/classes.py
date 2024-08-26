class person:
    name = "sneha"
    age = 21
    occupation = "sales executive"
a = person()  #instance of class
print(a.name)
print(a.age)
print(a.occupation)

a.name = "rahul"  #creating new object


print(f"my name is {a.name} , i am {a.age} years old and my occupation is {a.occupation}")
