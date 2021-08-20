
# Program to Print Grades
c=int(input("Enter C Language Marks:"))
java=int(input("Enter Java Programming Marks:"))
python=int(input("Enter Python Programming Marks:"))

total=c+java+python
avg=total/3

print("Total is:",total)
print("Average is:",avg)

if c>=40 and java>=40 and python>=40:
    if avg>=60:
        print("First Grade...")
    elif avg>=50:
        print("Second Grade...")
    else:
        print("Third Grade....")
else:
    print("No Grade")
    if c<40:
        print("Failed in C")
    if java<40:
        print("Failed in Java")
    if python<40:
        print("Failed in Python")


