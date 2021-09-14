
#Read N Subjects and Display Maximum and Minimum Marks without using max() and min() functions

N=int(input("Enter How Many Subjects...:"))

marks=[]

for i in range(1,N+1):
    m=int(input(F"Enter Subject {i} Marks:"))
    marks.append(m)

print("U Have Secured the Following marks:")
print(marks)

marks=sorted(marks)

print("type of marks is:",type(marks))
print("Minimum Marks are:",marks[0])
print("Maximum Marks are:",marks[-1])