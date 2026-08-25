products = {
    "pen":10, 
    "pencil":5,
    "car":100,
    "bus":300,
    "bike":20
    }
sum=0
for key,value in products.items(): 
    sum+=value
    print(key,value)
print(f"the total sum of products is : {sum}")
