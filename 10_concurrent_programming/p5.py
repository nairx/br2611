import time 
from threading import Thread 

def download_file(name):
    print(f"Starting {name}")
    time.sleep(3)
    print(f"Finish {name}")
start = time.time()
t1 = Thread(target=download_file,args=("file1.txt",))
t2 = Thread(target=download_file,args=("file2.txt",))
t1.start()
t2.start()
t1.join()
t2.join()
print("All files are downloaded!")

