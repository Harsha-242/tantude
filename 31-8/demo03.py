prices = {"milk": 2, "bread": 1, "eggs": 3}
for item, price in prices.items():
    print(f"{item}: rupees{price}")

total_cost = sum(prices.values())
print(f"Total Cost of all items: ${total_cost}")
