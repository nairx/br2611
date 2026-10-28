import sys
def numbers():
    return [x for x in range(1000)]
result1 = numbers()
print(sys.getsizeof(result1," bytes"))

def numbers():
    for x in range(1000):
        yield x
result2 = numbers()
print(sys.getsizeof(result2," bytes"))
