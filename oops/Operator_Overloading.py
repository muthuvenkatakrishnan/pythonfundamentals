a = 10
b = 20

print( a + b)
a = "Hello "
b = "World!"

print( a+b)


class Operate:

    def __init__(self, a):
        self.a = a

    def __add__(self, val):
        return self.a + val.a

ob1 = Operate(int(input("Enter a number")))
ob2 = Operate(int(input("Enter a number")))
print(type(ob1))
print(ob1+ob2)

ob1 = Operate(input("Enter a number"))
ob2 = Operate(input("Enter a number"))

print(ob1+ob2)

