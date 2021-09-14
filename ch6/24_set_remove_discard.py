
# create a set with some elements and apply remove() and discard() function

s={12,34,67,"Raj","Raj",900}
print(s)

if 999 in s:
    s.remove(999)
else:
    print ("999 is not there in set")

s.discard(888)

print(s)