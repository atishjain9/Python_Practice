
# Read 10 nos and display unique numbers

no=[]

for i in range(1,11):
    no.append(int(input(F"Enter {i} no:")))

s=set(no)

print("The Elements of set s are:",s)
print("The Elements of set in Ascending order are:",sorted(s))
print("The Elements of set in Descending order are:",sorted(s,reverse=True))