# # file = open("student.txt", "r")



# # print(file.read())

# # file.close()

# with open("student.txt","r") as file:
#     print(file.read())
with open("student.txt","w") as file:
    file.write("mahi")

with open("student.txt", "r") as file:
    print(file.read())

