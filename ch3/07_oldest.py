
# Program to Find oldest person from their inputted age

age1=int(input("Enter First Person Age:"))
age2=int(input("Enter Second Person Age:"))
age3=int(input("Enter Thrid Person Age:"))

if age1>age2 and age1>age3:
    print(F"Elder one is First Person and His age is {age1} years")
elif age2>age3:
    print(F"Elder one is Second Person and His age is {age2} years")
else:
    print(F"Elder one is Thrid Person and His age is {age3} years")