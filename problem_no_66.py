#appproach1
thislist = [15,20,15,20,21]
for i in thislist:
    if thislist.count(i) == 1:
        print(i)


#approach 2
thislist = [ 15, 20, 15, 20, 21 ]
sum = 0
for i in thislist:
    sum = sum ^ i
print(sum)


#approch3
thislist = [ 15, 20, 15, 20, 21 ]
dict = {}
for i in thislist:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print(i)


