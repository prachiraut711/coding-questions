# 2nd smallest
n = int(input())
arr = list(map(int,input().split()))
first_min = float("inf")   #the positive inf getl
second_min = float("inf")
for i in range(len(arr)):
    if arr[i] < first_min:
        second_min = first_min
        first_min = arr[i]
    elif arr[i] < second_min and arr[i] != first_min:
        second_min = arr[i]
print(second_min)



# Step 1: Input and storage
students = []
for _ in range(int(input("Enter number of students: "))):
    name = input("Enter student's name: ")
    grade = float(input("Enter student's grade: "))
    students.append([name, grade])

# Step 2: Extract unique grades and find the second lowest
grades = sorted(set([student[1] for student in students]))
second_lowest_grade = grades[1]

# Step 3: Find students with the second lowest grade
second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]

# Step 4: Sort alphabetically and print
second_lowest_students.sort()
for student in second_lowest_students:
    print(student)
