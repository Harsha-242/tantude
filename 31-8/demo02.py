fruits = {"apples": 10, "bananas": 6}
print(fruits)
fruits["oranges"] = 15

fruits["apples"] = 12
print(fruits)

removed_value = fruits.pop("bananas")

print("Updated fruits:", fruits)
print("Removed Bananas Count:", removed_value)
