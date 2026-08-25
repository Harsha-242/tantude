vowles="aeiouAEIOU"
s=input("enter ur words : ")
count=set()
for lettres in s:
    if lettres in vowles:
        count.add(lettres.lower())
print(len(count))        
       
