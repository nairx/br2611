from collections import deque
name = deque(["Amy","John"])

# name.append("Chastity")
# name.appendleft("Mike")
# print(name)

name.extend(["Mickey","Shawn"])
name.extendleft(["Mike","Cathy"])

print(name)