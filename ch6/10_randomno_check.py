
#Generate Random numbers and check if key no exists and how many times it exists

import random
n=[]

for i in range(1,10):
    n.append(random.randint(1,10))

tuple_random=tuple(n)

print("Random Elements from the Tuple are:",tuple_random)

key=int(input("Enter key element to find:"))

if key in tuple_random:
    print(F"{key} is found {tuple_random.count(key)} no of times....")
else:
    print(F"{key} is not found")