def display():
    print("Testing lambda")

msg = lambda:print("Testing Lambda")
print(msg())


def add(num):
    x = num + 15
    print(x)
add(5)

x = lambda num: num + 15
print(x(5))

powers = lambda b, e: b ** e
print(powers(2,6)) 

find_big = lambda a,b,c: f"a: {a}" if a>b and a>c else f"b: {b}" if b>c else f"c: {c}"
print(find_big(10,45,233))