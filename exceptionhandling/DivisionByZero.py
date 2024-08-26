for i in range(10):
    try:
        print(10 / i)
    except ZeroDivisionError:
        print("Division by zero is not allowed")
else:
    print("Division completed successfully")