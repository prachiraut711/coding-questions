# Que: 

l = ['a', 'b', 'c', 'd']

letter = 'c'

# Approach 1
# if letter in l:
#     print("yes")
# else:
#     print("no")

# Approach 2
found = False
for item in l:
    if item == letter:
        found = True
        break 
if found:
    print("The letter is in the list.")
else:
    print("The letter is not in the list.")


#  Approch3
found = False
index = 0
while index < len(l):
    if l[index] == letter:
        found = True
        break
    index += 1
if found:
    print("yes")
else:
    print("no")