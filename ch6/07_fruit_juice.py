
# Program to Read 5 fruits in tuple and update with fruit_name+ Juice
fruits=[]
for i in range(1,6):
    fruits.append(input(F"Enter Fruit name {i}:"))

fruits=tuple(fruits)
print("Furits from the Tuple are:",fruits)

fruit_juice=list(i+" Juice" for i in fruits )

fruit_juice=tuple(fruit_juice)
print("Fruits from the Tuple are:",fruit_juice)
