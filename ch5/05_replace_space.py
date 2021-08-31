
#program to find and replace double space

str=input("Enter a string....:")

pos=str.find("  ")
if pos>0:
   str=str.replace("  "," ")
   print(str)
else:
    print("Double Space not found....")