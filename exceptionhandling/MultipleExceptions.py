a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
try:
    print(a/b)
    print('10'+40)
except (TypeError, ZeroDivisionError):
    print("Exception occurred")
print("thank you")