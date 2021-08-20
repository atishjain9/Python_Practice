#Program to Generate Bill for the customer

cost=int(input("Enter Cost of the Mobile...:"))
mode=input("Are You Paying cash(y/n):")

discount=extra=0

if mode=="y" or mode=="Y":
    discount=cost*25/100
    billamt=cost-discount
elif mode=="n" or mode=='N':
    days=int(input("In How Many Days Will you Pay...:"))

    if(days<7):
        discount=cost*15/100
        billamt=cost-discount
    else:
        extra=cost*10/100
        billamt=cost+extra
else:
    print("Please Provide Correct Input...")

if discount>0:
    print("Discount Amount is:",discount)
    print("Final Bill Amount is:",billamt)
elif extra>0:
    print("Extra Amount is:",extra)
    print("Final Bill Amount is:",billamt)
else:
    print("No Bill to Generate")