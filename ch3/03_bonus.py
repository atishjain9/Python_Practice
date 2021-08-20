#Program to Calculate Bonus based on Year of Service

salary=eval(input("Enter ur Salary..:"))
service=int(input("Enter ur Service in years....:"))

if service>5:
    bonus=salary*10/100
    print(F"Bonus is: {bonus}")
else:
    print("Sorry Ur Not Eligible for Bonus....")