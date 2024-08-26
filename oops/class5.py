#create a class called as phone with attributes for "type" and "brand". 
#create a method for both the attribues, create instance for class phone and 
# print the type and brand. 

class Phone:
    def __init__(self, type, brand):
        self.type = type
        self.brand = brand

    def get_type(self):
        print(f"The type is {self.type}")
    
    def get_brand(self):
        print(f"The brand of the phone is {self.brand}")

p = Phone("smartphone", "Redmi")

p.get_type()
p.get_brand()

        