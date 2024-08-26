# whenever an error (syntax) occurs, the program stops and there will be
# error message displayed on the console.

# First line says that it is a traceback. It means that the interpreter
# traces the lines of code back to its source.

# Second line says that there is an error in the <filename> and which line
# causes that error.

# Third line says which statement is triggering that error.

# Fourth line says what is the error message. It also says the type of
# the error or the exception that occurred.

class Mouse:
    pass

# print(Mouse.wheels) # AttributeError: type object 'Mouse' has no attribute 'wheels'
# print(10/0)# ZeroDivisionError: division by zero

lst = [1,2,3]
#print(lst[3]) # IndexError: list index out of range

name = "John"
print(name[10]) # IndexError: string index out of range