import random
images = ["rock" , "paper" , "scissor"]
my_choice = int(input("enter '0' for rock , '1' for paper and '2' for scissor"))
print(images[my_choice])

comp_choice = random.randint(0,2)
print(images[comp_choice])

if (my_choice>2) or (my_choice<0):
    print("invalid")

    print("draw")
elif (my_choice == 0) and (comp_choice == 2):
    print("i win")
elif (my_choice == 2) and (comp_choice == 0):
    print("i lose")
elif my_choice > comp_choice:
    print(" i win")
elif my_choice < comp_choice:
    print("i lose")
else:
    print("its a draw")

