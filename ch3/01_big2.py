# Biggest of two numbers

no1=int(input("Enter First no....:"))
no2=int(input("Enter Second no....:"))

if no1>no2:
    print("Biggest no is:",no1)
else:
    if no2>no1:
        print("Biggest no is:",no2)
    else:
        print("Both Numbers are Similar....")
