
# Program to Print Table no

no=int(input("Enter Table no:"))
tar=int(input("Enter ur Target Value:"))

for i in range(1,tar+1):
    print(F"{no} * {i} = {i*no}")