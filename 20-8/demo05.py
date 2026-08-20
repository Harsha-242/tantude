student=["anand","kishore","junir","jdnfi"]
d={a:len(a) for a in student}
print(d)

marks=[25,34,94,93]
student_marks={}
for i in range(1,len(student)):
    student_marks[student[i]]=marks[i]
    print(student_marks)
print(student_marks)