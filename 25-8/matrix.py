rows=int(input("enter the number of rows : "))
columns=int(input("enter the number of columns : "))
matrix=[]

for i in range(rows):
    row=[] 
    for j in range(columns):
        x = int(input("enter the element : "))
        row.append(x)
    matrix.append(row)
   
print(matrix)