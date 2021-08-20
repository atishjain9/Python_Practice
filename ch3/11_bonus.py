#Program to check for bonus eligibility
ms=input("Enter Marital status([M]arried/[U]n-Married):")
if(ms=='M' or ms=='m'):
    print("Ur Eligible for Bonus....")
elif (ms=='U' or ms=='u'):
        gen=input("Enter ur Gender([M]ale/[F]emale):")
        age=int(input("Enter ur Age...:"))

        if(gen=="M" or gen=="m"):
            if(age>=30):
                print("Ur Eligible for Bonus...")
            else:
                print("Ur Not Eligible for Bonus...")
        elif (gen=='F' or gen=='f'):
            if(age>=25):
                print("Ur Eligible for Bonus...")
            else:
                print("Ur Not Eligible for Bonus...")
        else:
            print("Pls Provide Valid Gender...")
else:
    print("Pls Enter Correct Status....")