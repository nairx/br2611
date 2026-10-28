def deco(fnc):
    def wrapper():
        print("Begin")
        fnc()
        print("End")
    return wrapper

@deco
def f1():
    print("Hello World")

@deco
def f2():
    print("Good Morning")

f1()
f2()

# def f1():
#     print("Begin")
#     print("Hello World")
#     print("End")

# def f2():
#     print("Begin")
#     print("Good Morning")
#     print("End")

# f1()
# f2()