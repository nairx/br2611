
import schedule 
import time 

def my_task():
    print("Task Executed")

# schedule.every(2).seconds.do(my_task)
schedule.every().day.at("14:35").do(my_task)

while True:
    schedule.run_pending()
    time.sleep(1)

