class Products:

    def __init__(self):
        print("Products Created")
    
    def __del__(self):
        print("Products deleted")

def create_Product():
    print("Preparing for object creation")
    pr = Products()
    print("Done with the execution of function")
    return pr

p = create_Product()
print(f"The object created using the function is: {p}")
print("End of code")