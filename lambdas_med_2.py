students = [('Alice', 85), ('Bob', 90), ('Charlie', 78)]

#SORTING USING LAMBDA

#sort by

#Grade

by_grade = sorted(students, key=lambda student: student[1])
print(by_grade)

#Name Length

by_name_len = sorted(students, key= lambda student: len(student[0]))

#Grade in descending order

by_grade_desc = sorted(students, key = lambda student: student[1], reverse=True)
print(by_grade_desc)