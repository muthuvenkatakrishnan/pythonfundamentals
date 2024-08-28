import _thread
import time
def find_circle_area(num):
    print("Area of the circle for the given radius is:")
    for radius in num:
        area = 3.14 * radius * radius
        print(f"Radius: {radius} -> Area: {area}")

def find_square_area(num):
    print("Area of the square for the given side is:")
    for side in num:
        area = side * side
        print(f"Side: {side} -> Area: {area}")

start_time = time.time()
_thread.start_new_thread(find_circle_area, ([5, 10, 15, 20, 25],))
print(f"Time taken for the execution: {time.time() - start_time}" )
_thread.start_new_thread(find_square_area, ([5, 10, 15, 20, 25],))
