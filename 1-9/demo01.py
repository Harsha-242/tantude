fruits = ["apple", "banana", "cherry"]
print("First fruit:", fruits[0])
fruits[1] = "blueberry"
fruits.append("orange") 
fruits.remove("cherry")
print("Current list:")
for fruit in fruits:
    print("-", fruit)
