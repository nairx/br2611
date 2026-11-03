from multiprocessing import Process 
from time import sleep 
import os 
def calculate(number):
    print("Child PID",os.getpid())
    sum = 0
    for i in range(number):
        sum += i
    print(sum)
    sleep(10)

if __name__ == "__main__":
    print("Main Process",os.getpid())
    p1 = Process(target=calculate,args=(1_000_000,))
    p2 = Process(target=calculate,args=(1_000_000,))
    p3 = Process(target=calculate,args=(1_000_000,))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()