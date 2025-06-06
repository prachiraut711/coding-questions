#Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
#5(sample input)
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output 0
# Berry
# Harry

thislist = []
for i in range (int(input())):
    name = input()
    score = float(input())
    thislist.append([name, score])

first_max = float("inf")
second_max = float("inf")
for i in range(len(thislist)):
    if thislist[i][1] < first_max:
        second_max = first_max
        first_max = thislist[i][1]
    elif thislist[i][1] < second_max and thislist[i][1] != first_max:
        second_max = thislist[i][1]

sorted_list = []
for i in range(len(thislist)):
    if second_max == thislist[i][1]:
        sorted_list.append(thislist[i][0])
sorted_list.sort()
for i in sorted_list:
    print(i)
