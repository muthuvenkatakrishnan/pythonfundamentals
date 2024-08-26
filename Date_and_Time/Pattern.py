import time
import sys

def pattern(n):
    for i in range (1,n+1):
        for j in range (1,i+1):
            sys.stdout.write("* ")
            sys.stdout.flush()
            time.sleep(0.5)
        print()

def printSentence(msg):
    for c in msg:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.5)

def printVal(n):
    for i in range (1,n+1):
        sys.stdout.write(f"{i}")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write(".")
        
printVal(5)