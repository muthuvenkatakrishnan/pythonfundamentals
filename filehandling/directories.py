import os

# Displaying the current working directory
mywd = os.getcwd()
print(type(mywd))

# Displaying the current working directory as string
print(os.getcwdb())
uwd = os.getcwdb()
print(type(uwd))

# Changing the current working directory
# chdir() will not create a new directory if it does not exist
# It will raise an error if the directory does not exist
# It is used to change the current working directory only

os.chdir("D:/Python/Python-File-Handling")

# Displaying the current working directory
print(os.getcwd())

# List the contents of the current working directory
print(os.listdir())

# Creating a new directory
os.mkdir("test")

# List the contents of the current working directory
print(os.listdir())




