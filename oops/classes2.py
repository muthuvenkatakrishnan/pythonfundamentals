#using method
class person:
    name = "harish"
    age = 24
    occupation = "developer"

    def info(self):
        print(f"my name is {self.name} , my age is {self.age} , and i am a{self.occupation}")
a = person()   #creating instance for object called as 'a'
b = person()
c= person()
a.info()
b.name = "swati"
b.age = 23
b.occupation = "tester"
b.info()
c.info()







           
