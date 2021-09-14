
# Example on Dictionary
mydict={
        "Keyboard":"Its an Input Device",
        "Monitor":"Its an Output Device",
        "Mic": "Its an Input Device",
        "Speakers" : "Its an Output Device",
        "Pendrive:": "Its an Input & Output Device",
        "Touch-Screen":"Its an Input & Outtput Device"
}

print("List of Items are...:",mydict.keys())
a=input("Select an Item...:")

if a in mydict:
    print(F"{a} - {mydict.get(a)}")
else:
    print(F"{a} not found")
