from multiprocessing import Process 
from time import sleep 
import os 

def calculate(number):
    print("Child PID",os.getpid())
    for i in range(number):
        pass

if __name__ == "__main__":
    print("Main Process",os.getpid())
    p1 = Process(target=calculate,args=(1_000_000,))
    p1.start()
    p1.join