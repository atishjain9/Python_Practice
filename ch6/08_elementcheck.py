
# Program to check whether an key element exists in a tuple or not with count

nos=(10,20,30,40,50,60,50,100,50,100)
print("Length of the Tuple is:",len(nos))
print("Elements of the tuple are:",nos)

key=int(input("Enter Key Element to Search...:"))

if key in nos:
    print(F"{key} is found {nos.count(key)} no of times")
else:
    print(F"{key} is not found....")
