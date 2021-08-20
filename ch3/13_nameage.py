
#Program to check who is elder based on age

name1=input("Enter ur Name...:")
age1=int(input("Enter ur Age..:"))

name2=input("Enter ur Name...:")
age2=int(input("Enter ur Age..:"))

if(age1>age2):
    print(F"{name1} is Elder than {name2}")
elif (age2>age1):
    print(F"{name2} is Elder than {name1}")
else:
    print(F"{name1} and {name2} both are of similar age")