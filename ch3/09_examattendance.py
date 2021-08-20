
# Allow Student to Write the Exam based on Attendance

noc=int(input("Enter the Total Number of Classes Held:"))
noa=int(input("Enter the Total Number of Classes Attended:"))

per=(noa/noc)*100

print("Attendance Percentage is:%.2f"%per)

if per>=75:
    print("Ur Allowed to Write the Exam...")
else:
    mc=input("Do you Have Medical Certificate(y/n):")
    if mc=='y':
        print("U Have Medical Certificate, so you can write the Exam...")
    else:
        print("U Dont Have Medical Certificate, so you canot write the Exam...")