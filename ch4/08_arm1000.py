
#printing armstrong nos till 1000
for no in range(0,1000): # generates nos till 1000
    r=0
    sum=0
    temp=no
    while no>0: #checks no is armstrong or not
        r=no%10
        sum=sum+(r*r*r)
        no=no//10
    no=temp
    if no==sum: #prints the armstrong no
        print(no)
