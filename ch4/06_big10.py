
# Program to find biggest of 10 numbers

count=1
big=0
while count<=10:
    no=int(input(F"Enter {count} no...:"))

    if no>big:
        big=no
    count+=1
print("Biggest no is:",big)
