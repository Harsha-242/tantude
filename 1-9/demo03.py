# numbers = [45, 22, 89, 14, 67, 98, 3]
# max_num = max(numbers)
# min_num = min(numbers)
# print(f"Largest: {max_num}, Smallest: {min_num}")

numbers = [45, 22, 89, 14, 67, 98, 3]
max_num = numbers[0]
min_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num 
    if num < min_num:
        min_num = num  
print(f"Largest: {max_num}, Smallest: {min_num}")
