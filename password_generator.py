import random
letters = ['a' , 'b' , 'c' , 'd' , 'e' , 'f']
symbols = ['!' , '@' , '#' , '$' , '%']
numbers = ['1','2','3','4','5','6','7','8','9','0']

n_letters = int(input("how many letters?"))   #4
n_symbols = int(input("how many symbols?"))
n_numbers = int(input("how many numbers?"))
                      

password = " "
for char in range(n_letters): #4
    password += random.choice(letters)
for char in range (n_symbols):
    password += random.choice(symbols)
for char in range(n_numbers):
    password += random.choice(numbers)

print(password)




