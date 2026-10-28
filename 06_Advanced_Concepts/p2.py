import sys

def numbers():
    return [1,2,3]

result = numbers()
for i in result:
    print(i)


def numbers():
    yield 1
    yield 2
    yield 3
result = numbers()
for i in result:
    print(i)