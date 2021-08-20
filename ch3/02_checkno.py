#Program to Check Whether the no is Positive, Negative or Neutral

no=int(input("Enter a no....:"))

if no>0:
    print(f"{no} is Positive....")
else:
    if no<0:
        print(f"{no} is Negative...")
    else:
        print(f"{no} is Neutral....")
