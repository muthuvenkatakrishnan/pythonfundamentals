def numerical_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

num1 = numerical_input("Enter the first number: ")
num2 = numerical_input("Enter the second number: ")

total = num1 + num2
print(f"The sum of {num1} and {num2} is {total}.")