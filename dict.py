students = {}
size = int(input("enter the number of students:"))
for i in range(size):
    stu_name = input("enter the student name:")
    course = input("enter the course:")
    course_fees = int(input("enter the course fees:"))
    students[stu_name] = {}
    students[stu_name]["course"] = course
    students[stu_name]["fees"] = course_fees

print("students dictionary is :")
print(students)

print("students who have taken python:")
for key , val in students.items():
    if val["course"] == "python":
        print(key)