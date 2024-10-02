n = int(input("Number of students: "))

lst_grade = []

for i in range(n):
    name = input("Enter your name: ")
    grade = int(input("Enter your grade: "))
    lst_grade.append({"name":name, "grade":grade})

for item in lst_grade:
    print(item)