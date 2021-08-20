
# Program to Print Grades based on Average Marks

avg=float(input("Enter ur Average Marks...:"))

print("Grade is:",end=" ")
if avg>=90:
    print("A+")
elif avg>=80:
    print("A")
elif avg>=70:
    print("B+")
elif avg>=60:
    print("B")
elif avg>=50:
    print("C")
else:
    print("Failed")
