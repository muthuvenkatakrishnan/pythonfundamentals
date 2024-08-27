a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
try:
    print(a/b)
    print('10'+'40')
    ad = [1,2,3,4,5]
    print(ad[1])
except TypeError:
    print("Type error occurred")
except ZeroDivisionError:
    print("Division by zero is not allowed")
except:
    print("Exception occurred")
finally:
    print("This is always executed")
    
print("thank you")