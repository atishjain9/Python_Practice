#Program to check for leap year
year=int(input("Enter a year...:"))

if(year%100==0):
    if(year%400==0):
        print(year,"its a leap year..")
    else:
        print(year,"Its Not a leap year")
else:
    if(year%4==0):
        print(year,"Its a leap year...")
    else:
        print(year,"Its Not a leap year")