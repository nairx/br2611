
try:
    a = [5,6,7]
    print(a[9])
except (NameError):
    print("Name Error")
except (ZeroDivisionError):
    print("Cannot divide by zero")
except:
    print("Something wrong")


# try:
#     print(a)
# except:
#     print("Something went wrong")
# else:
#     print("No Error")
# finally:
#     print("Program Completed")