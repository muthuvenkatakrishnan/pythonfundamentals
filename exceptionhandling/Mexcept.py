a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
try:
    print(a/b)
    print('10'+40)
except TypeError:
    print("Type error occurred")
except ZeroDivisionError:
    print("Division by zero is not allowed")
    b = int(input("Enter another number: "))
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Division by zero is not allowed and program is terminated")
print("thank you")