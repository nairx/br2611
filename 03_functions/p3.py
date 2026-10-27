# result = [True,False,True,True]
# print(any(result))
# print(all(result))

score=[45,67,90,50]
result = [x>40 for x in score]
if all(result):
    print("Pass")
else:
    print("Fail")


# score=[45,67,90,10]
# for i in score:
    

# score=[45,67,90,15]
# result="passed"
# for i in score:
#     if i>40:
#         continue
#     else:
#         print("Failed")
#         break
# print(result)


# score = [40, 75, 88, 12]
# result = 'Pass'
# for s in score:
#     if s < 40:
#         result = 'Fail'
#         break

# print(result)

score = [40, 75, 88, 52]
for s in score:
    if s < 40:
        print("Fail")
        break
else:
    print("Pass")



# score=[45,67,90,55]
# result="passed"
# for i in score:
#     if i<40:
#         print("Failed")
#         break
# print(result)
 



# numbers = [x for x in range(1,11)]
# print(numbers)