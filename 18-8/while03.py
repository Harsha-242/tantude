condition = True
i=1;
while condition==True :
   if i%2!=0:
       i=i+1
       continue

   print(i)
   i=i+1
   if i>100:
      break
print("i give up")