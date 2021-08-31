
#Program to count uppercase letter, lowercase letters, digits and special characters
import sys

email=input("Enter ur Email id:")

for i in email:
    if i.isspace():
        print("Email cannot have Spaces, Program Exiting....")
        sys.exit(0)

u=l=d=s=0

for ch in email:
    if ch.isupper():
        u+=1
    elif ch.islower():
        l+=1
    elif ch.isdigit():
        d+=1
    else:
        s+=1

print("Uppercase Letters count:",u)
print("Lowercase Letters count:",l)
print("Digits count:",d)
print("Special Characters count:",s)
