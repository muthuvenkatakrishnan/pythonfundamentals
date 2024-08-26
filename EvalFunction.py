a = 10
b = 15
print("(a+b)^2")
print(eval('a**2 + b**2 + 2*a*b'))

def hack_your_password():
    password = "Pd3#%&eR0"
    print(f"The password is: {password}")


expr = input('Enter an expression')
dictionary = {}
dictionary['x'] = expr
# eval(expr,dictionary)
eval(expr)
