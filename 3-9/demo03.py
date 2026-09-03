mytuple=("apple", "banana", "bow", "date", "elderberry")
print(mytuple)

mylist=list(mytuple)
print(mylist)      #['apple', 'banana', 'bow', 'date', 'elderberry']

for o in range(len(mylist)):
    mylist[o]=mylist[o].upper()
print(mylist)
mytuple=tuple(mylist)
print(mytuple)