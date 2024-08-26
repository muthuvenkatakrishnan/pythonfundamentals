class dog:
    breed = "german"  #class variable

    def __init__(self , name , age):
        self.name = name    #instance variables
        self.age = age

dog1 = dog("tiger" , 5) 
print(dog.breed)
#classname.classVariableName, while printing/accessing class variables
print(dog1.name)  
print(dog1.age)
#intance.instanceVraiableName for accessing values of instance

