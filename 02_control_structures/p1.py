# i=0
# while i<10:
#     print(i)
#     i=i+1

# i=0
# while i<10:
#     print(i)
#     i=i+1
#     if i==5:
#         break

# while True:
#     name = input("Enter name: ")
#     print("Hello " + name)
#     choice = input("Do you want to Continue?(y/n)")
#     if choice != 'y':
#         break

# i=0
# while i<10:
#     i=i+1
#     if i==5:
#         continue
#     print(i)

i=0
while i<5:
    name = input("Enter name: ")
    print("Hello " + name)
    choice = input("Do you want to Continue?(y/n)")
    if choice != 'y':
        break
    i=i+1
else:
    print("Loops completed successfully")