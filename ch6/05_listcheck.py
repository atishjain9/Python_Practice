
# Read elements in the list and display
item=[]
N=int(input("Enter How many Items you want to store in the list:"))

for i in range(1,N+1):
    item.append(input(F"Enter Item {i}:"))

if not item:
    print("List is Empty....")
else:
    print("List of Items are:",item)