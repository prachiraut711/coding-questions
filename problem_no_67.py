#remove zero from list and insert them at last

thislist = [1, 0, 3, 0, 0, 4, 5]
for item in thislist:
    if item == 0:
        thislist.remove(item)
        thislist.append(item)
print(thislist) 