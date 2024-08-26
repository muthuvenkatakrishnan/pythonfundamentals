#using constructor
class dog:
    def __init__(self,name , age):  #attributes
        self.name = name
        self.age = age

    def display_info(self):
        print(f"name = {self.name} and age is {self.age}")

a = dog("buddy", 5)
a.display_info()


