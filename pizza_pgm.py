print("thank u for chosing pizza deliveries")
bill = 0
size = input("enter 's' , 'm' or 'l' :")
add_pepp = input("if u want pepp then 'y' or 'n' ")
cheese = input("if u want cheese then 'y' or 'n' ")
if size == 's':
    bill +=15
elif size == 'm':
    bill += 20
else:
    bill += 25

if add_pepp == 'y':
    if size == 's':
        bill += 2
    else:
        bill

if cheese == 'y':
    bill += 1

print(f"total cost is {bill}")