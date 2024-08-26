#static method:
#shared among all instances of a class, similar to class variables.
#they are used withinb static methods.
#they dont recieve the default frst argument as 'self'

class dog:
    breed = "german"   

    @staticmethod
    def a():
        return "dog says woof!" 
#accessing static method   
print(dog.a())

