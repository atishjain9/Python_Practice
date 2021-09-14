#Remove Last Element from the Tuple

t1=(10,20,"Raj",12.50,"Muskan")
print("Elements of the Tuple are:",t1)

l1=list(t1) #convert tuple into list

print("Last Removed Element is:",l1.pop())
t1=tuple(l1)
print("Elements of Tuple are:",t1)