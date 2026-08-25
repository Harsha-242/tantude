import math
def is_prime(n):

   if n <= 1:
       return False
   for i in range(2, int(math.sqrt(n)) + 1):
       if n % i == 0:
           return False
   return True
num = 20
if is_prime(num):
   print(f"{num} is a prime number")
else:
   print(f"{num} is not a prime number")
   #{"Santhosh":2,"Harsha":2,"Straight":1}