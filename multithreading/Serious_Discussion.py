import multiprocessing as spoorthi
import math as suhas
from multiprocessing import Process as charu_roopa
import time as chetana

def display():
    chetana.sleep(2)
    print("Hello from display function. Please wake up")

def dis(name):
    for names in name:
        print(f"Hello {names}. Tomorrow please take up all the sessions and I will be on leave")

def sqroot(num):
    print(suhas.sqrt(num))

if __name__ == "__main__":
    pr1 = charu_roopa(target=display)
    pr2 = charu_roopa(target=dis, args=(["Suhas", "Charu Roopa","Chetana","Spoorthi"],))
    pr3 = charu_roopa(target=sqroot, args=(25,))
    pr1.start()
    pr2.start()
    pr3.start()
    pr1.join()
    print("Process is completed")