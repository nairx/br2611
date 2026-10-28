from datetime import datetime,date,timedelta
# dt = date.today()
# tomorrow = dt + timedelta(days=1)
# yesterday = dt - timedelta(days=1)
# print(dt)
# print(tomorrow)
# print(yesterday)

t1 = datetime(2027,1,1)
t2 = datetime.now()

d = t1-t2

print(d.days)