def intro(**data):
    print("Arbitrary Keyword Argument")
    print("The data type of data is: ", type(data))
    for key, value in data.items():
        print(f"{key} is {value}")

intro(Empid = 123, Designation = "Developer", Salary = 35445, Age = 34)
intro(Empid = 233, Designation = "Designer", Salary = 33545, Age = 36)
intro(Empid = 343, Designation = "Business Analyst", Salary = 63445, Age = 24, Department = "Operations")

# *args & **kwargs
#-----------------

# Both *args and **kwargs are special keywords that allows the function to take variable
# length argument

# *args represents a variable that takes n number of arguments in the form of tuple

# **kwargs represents a varaible that takes n number of keyword driven arguments 
# in the form of dictionary  

# It makes the function flexible in nature