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

with open("students.txt",'a') as file:
    file.write("Cathy\n")