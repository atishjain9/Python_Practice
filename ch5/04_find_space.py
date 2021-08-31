
# Program to Detect double space from the inputted string

str=input("Enter a string....:")

pos=str.find("  ")
if pos>0:
    print("Double Space found at Index %d "%pos)
else:
    print("Double Space not Found")