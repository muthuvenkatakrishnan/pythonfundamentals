class Alpha:
    def display(self):
        print("Hello")
class Beta (Alpha):
    def display(self):
        print("Welcome")
    
    def show(self):
        print("Show method")
class Charlie (Beta):
    
    def display(self):
        print("Charlie Display")

    def show(self):
        print("Charlie Show method")
    
ch = Charlie()
ch.display()
ch.show()