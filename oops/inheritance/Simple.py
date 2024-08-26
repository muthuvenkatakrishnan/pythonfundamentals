age = 0
class Person:
    
    def __init__(self):
        global age
        age += 10
        print("Person class Constructor")

class Employee(Person):
    
    def __init__(self):
        super().__init__()
        global age
        age += 10
        print("Employee class Constructor")


print(age)
muthu = Employee()
print(age)

class Furniture:
        def display(self):
             self.make = "Wood"
class Table (Furniture):
        def display(self):
             self.make = "Steel"

t = Table()
t.display()
print(t.make)