from concurrent.futures import ThreadPoolExecutor
import time 

def download_file(name):
    print(f"Starting {name}")
    time.sleep(3)
    return f"Finish {name}"


with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(download_file,["file1.txt","file2.txt","file3.txt","file4.txt","file5.txt"])
    for result in results:
        print(result)