
# program to check whether the inputted no is armstrong or not

r=0
sum=0
no=int(input("Enter a no...:"))
temp=no

while no>0:
    r=no%10
    sum=sum+(r*r*r)
    no=no//10

no=temp
if no==sum:
    print(F"{no} is Armstrong no")
else:
    print(F"{no} is Not a Armstrong no")