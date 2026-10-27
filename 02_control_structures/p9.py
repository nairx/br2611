result = {
 "maths": 3,
 "english": 25,
 "science": 5
}

print(max(result.values()))

print(max(result,key=result.get))

