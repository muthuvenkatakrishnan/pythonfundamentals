class dog:
    def __init__(self , name , age):
        self.name = name    #instance variables
        self.age = age

dog1 = dog("tiger" , 5)   #creating instance
print(dog1.name)  #print statement
print(dog1.age)