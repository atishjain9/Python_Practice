
#Program to Absolute Difference of two positive inters

n1=int(input("Enter a Positive no:"))
n2=int(input("Enter another Positive no:"))

if(n1>n2):
    diff=n1-n2
else:
    diff=n2-n1

print(F"Absolute Different of {n1} and {n2} is {diff}")
