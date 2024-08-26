class Emp:

    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal
    
    def __lt__(self, obj):
        if self.sal < obj.sal:
            print(f"Current object {self} is less than {obj}")
        else:
            print(f"Current object {self} is greater than {obj}")

    def __str__(self):
        return self.name

emp1 = Emp(23,"Muthu",4567)
emp2 = Emp(12,"Sandesh",6783)

emp1 < emp2