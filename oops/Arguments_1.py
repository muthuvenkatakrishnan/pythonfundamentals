class Test:

    def display(self, *modi):

        print(modi)
    

t = Test()
t.display(10,56,89)
t.display("Muthu","Abilash","Rahul")
t.display(True)
t.display(34+6j)
t.display(100.45)

t.display(name = "Muthu", Designation ="Trainer")

mytup = 10,20,340
print(type(mytup))