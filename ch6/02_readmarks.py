
# Program to Read Marks in a list and find sum,max and min marks

marks=[]

for i in range(1,6):
    m=int(input(F"Enter Marks of Subject {i}: "))
    marks.append(m)

print("U Have Secured the Following marks:")
print(marks)

print("Total is:",sum(marks))
print("Maximum Marks :",max(marks))
print("Minimum Marks:",min(marks))
print("All the Subject Marks in Ascending order:",sorted(marks))