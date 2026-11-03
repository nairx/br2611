# file = open("students.txt",'w')
# file.write("John\n")
# file.write("Amy\n")
# file.write("Mike\n")
# file.close()

#better approach
# with open("students1.txt",'w') as file:
#     file.write("John\n")
#     file.write("Amy\n")
#     file.write("Mike\n")

# with open("students.txt",'a') as file:
#     file.write("Cathy\n")

# with open("students.txt",'r') as file:
#     data = file.read()
# print(data)


# with open("students.txt",'r') as file:
#     for line in file:
#         print(line)

# with open("students.txt",'x') as file:
#     file.write("Brian")

# with open("students.txt",'r+') as file:
#     data = file.read()
#     print(data)
#     file.write("John")
#     data = file.read()
#     print(data)


# with open("students2.txt",'a') as file:
#     file.write("Brian")

with open("students1.txt","r") as file:
     result = "Amy" in file 
     print(file.name)