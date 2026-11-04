from concurrent.futures import ProcessPoolExecutor
from time import sleep

def square(n):
    sleep(30)
    return n*n 

if __name__== "__main__":
    with ProcessPoolExecutor() as executor:
        results = executor.map(square,[1,2,3,4,5,6,7,8,9,10])
        for result in results:
            print(result)