# Program to read Student names and their favorite subjects
n1,s1=input("Enter ur Name and Favorite Language:").split()
n2,s2=input("Enter ur Name and Favorite Language:").split()
n3,s3=input("Enter ur Name and Favorite Language:").split()
n4,s4=input("Enter ur Name and Favorite Language:").split()
n5,s5=input("Enter ur Name and Favorite Language:").split()

studentdict={n1:s1,n2:s2,n3:s3,n4:s4,n5:s5}

print("Student Detals are:")
print("-------------------")
for sd in studentdict.items():
    print(sd)