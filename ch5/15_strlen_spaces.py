
#program to String length without spaces

str=input("Enter a String...:")
len=0

for i in str:
    if not i.isspace():
        len=len+1
print("Length of the String without spaces is:",len)

