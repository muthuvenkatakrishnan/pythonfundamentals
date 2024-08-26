import random
letters = ['a' , 'b' , 'c' , 'd' , 'e' , 'f']
symbols = ['!' , '@' , '#' , '$' , '%']
numbers = ['1','2','3','4','5','6','7','8','9','0']

n_letters = int(input("how many letters?"))   
n_symbols = int(input("how many symbols?"))
n_numbers = int(input("how many numbers?"))

password_list = []
for char in range(n_letters):
    password_list.append(random.choice(letters))
for char in range(n_symbols):
    password_list.append(random.choice(symbols))
for char in range(n_numbers):
    password_list.append(random.choice(numbers))
print(password_list)

random.shuffle(password_list)
print(password_list)

password = " "
for char in password_list:
    password += char

print(f"the generated password is {password}")

    



