import sys

mylist = [x for x in range(1000)]
myiterator = iter(mylist)

print(sys.getsizeof(mylist), " bytes")
print(sys.getsizeof(myiterator), " bytes")

print(mylist[0])

print(next(myiterator))
print(next(myiterator))