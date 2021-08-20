#Calculate discount based on Total Purchase

billamt=int(input("Enter Total Bill Amount...:"))

if billamt>=1000:
    dis=billamt*10/100
else:
    dis=billamt*5/100

finalbillamt=billamt-dis

print("Discount is:",dis)
print("Final Bill Amount is:",finalbillamt)