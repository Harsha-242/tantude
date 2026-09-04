with open("student.txt","a") as file:
    file.write("\nghambir")

with open("student.txt","r") as file:
    print(file.read())