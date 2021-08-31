
#Program to Insert Middle name in the Middle of first and last name

name=input("Enter First and Last Name:")
middle=input("Enter Middle name:")

pos=name.find(" ")
fullname=name[:pos+1]
fullname=fullname+middle
fullname=fullname+name[pos:]

print("Full Name is:",fullname)