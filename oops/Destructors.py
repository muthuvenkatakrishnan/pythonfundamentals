"""
A desctructor is defined as follows:

        def __del__(self):
            # implementation of destructor

Destructors are called when the object is derefrred or at the end of the execution

"""

class Employee:

    def __init__(self):
        self.age = 56
        print("Employe object is created")

    def display(self):
        print(self.age)
    
    def __del__(self):
        print("The destuctor is called and Employee object is deleted")

o = Employee()
o.display()
del o