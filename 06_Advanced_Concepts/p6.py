import time
def timer(func):
 def wrapper(*args, **kwargs):
  start = time.time()
  result = func(*args, **kwargs)
  end = time.time()
  print(f"Took {end - start:.4f} seconds")
  return result
 return wrapper

@timer
def calculate():
 total = 0
 for i in range(1_000_000):
  total += i
 return total

@timer
def add(a,b):
 print(a+b)

calculate()
add(a=3,b=2)
