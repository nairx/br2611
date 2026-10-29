from collections import namedtuple

Price = namedtuple('Price',["Product1", "Product2", "Product3"])

p = Price(100,120,140)

print(p.Product1)

