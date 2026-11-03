import csv 
# with open("students.csv",'w',newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name","Age"])
#     writer.writerow(["John",21])
#     writer.writerow(["Mike",20])
#     writer.writerow(["Amy",23])


# with open("students.csv",'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# with open("students.csv",'r') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row["Name"])

data = [
    {"Name":"Sherin","Age":23},
    {"Name":"Amy","Age":20},
]
with open("users.csv","w",newline="") as file:
    fieldnames = ["Name","Age"]
    writer = csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)