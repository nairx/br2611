from collections import ChainMap

court1 = {'Nada1':12,"Novak":10}
court2 = {"Osaka":10,"Sharapova":7}

result = ChainMap(court1,court2)

for key,value in result.items():
    print(key,value)