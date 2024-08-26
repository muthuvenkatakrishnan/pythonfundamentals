class rectangle:
    def __init__(self , width , height):
        self.width = width
        self.height = height

    def area(self):
        return (self.width * self.height)
    
    def perimeter(self):
        return 2+(self.width * self.height)
    

rect = rectangle(5 , 3)
rect1 = rectangle(8,4)
print(rect.area())
print(rect.perimeter())
print(rect1.area())
print(rect1.perimeter())

print(f"area is {rect.area()} perimeter is {rect.perimeter()}")



