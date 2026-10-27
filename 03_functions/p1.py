# def greet():
#     print("Greetings")
# greet()


# def add(a,b):
#     print(a+b)
# add(4,5)


# def add(a,b):
#     return a+b

# result = add(4,5)
# print(result)


# def add(a,b=0):
#     return a+b

# # result = add(4)
# # print(result)

# result = add(4,8)
# print(result)


# def add(a=0,b=0):
#     return a+b

# result = add()
# print(result)


# def add(a,b):
#     return a+b
# result = add(5,2)
# print(result)

# def add(a,b):
#     return a+b

# result = add(b=5,a=2)
# print(result)


# def add(a,b,c):
#     return a+b+c
# result = add(4,b=5,c=2)
# print(result)


# def add(*args):
#     return sum(args)


# result = add(4,5,8,8,9,6,5,4)
# print(result)


# def add(**kwargs):
#     return sum(kwargs.values())

# result = add(a=4,b=5)
# print(result)


def add(*args,**kwargs):
    print(args)
    print(kwargs)
    return sum(args)+sum(kwargs.values())

result = add(5,7,8,9,a=4,b=5)
print(result)


