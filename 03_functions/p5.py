# def sqr(x):
#     return x*x
# score = [5,6,8,4,2,4]
# result = map(sqr,score)
# print(list(result))


def f1(x):
    return x>4
score = [5,6,8,4,2,4]
result = filter(f1,score)
print(list(result))

