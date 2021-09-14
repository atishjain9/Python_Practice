
#Remove Empty tuples from the list
L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'),(), ('d')]

l1=[ t for t in L if t ]

print("List without empty tuples is:",l1)
print("Length of the list:",len(l1))