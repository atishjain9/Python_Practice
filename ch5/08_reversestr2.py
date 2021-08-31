
#program to Reverse the String using for while loop

str=input("Enter a string...:")
len=len(str)
revstr=""
len=len-1

while len>=0:
    revstr=revstr+str[len]
    len-=1
print("Revese String is:",revstr)



