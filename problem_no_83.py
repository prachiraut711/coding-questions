n = int(input())
student_marks = {}
for i in range(n):                 #we use split bcz aplyla name ani tyav=che score seperate karychet split nst kel tsr te sgal input ekch string zal ast mag te seperate karyla hard padl ast
    name, *line = input().split()  #input().split() reads a line of input, splits it into a list of strings (by whitespace), and then 
                                   #assigns the first element to name and the rest of the elements to line.The *line syntax is called
                                   #"extended unpacking" and it captures all remaining elements of the list into a new list named line
    scores = list(map(float, line))
    student_marks[name] = scores
print(student_marks)
query_name = input()
sum = 0
scores = student_marks[query_name]
if query_name in student_marks:
    for i in scores:
        sum += i
        avg = sum / len(scores)
print(avg)    #ithe output suppose om 10 10 10 mag avg = 10.0 al
              #pn mi jar print("%.2f" % avg)kel tar 10.00 yeil jar decimal decide karaycha asel liti gyayche tar as karaych.