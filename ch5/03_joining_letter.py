
# Program to Print Joining Letter
letter='''Dear <name>
You Admission for Python Programming Classes is Conformed !
Date of Joining: <date>

Thank you
Atish Jain
-Coding Career Expert'''

name=input("Enter ur Name...:")
doj=input("Enter Date of Joining:")

letter=letter.replace("<name>",name)
letter=letter.replace("<date>",doj)

print(letter)