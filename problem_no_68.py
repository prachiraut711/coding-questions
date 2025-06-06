#How can you access the first and last elements of a list?
thislist = [1 , 2 , 3 , 4 , 5]
first_element = thislist[0]
last_element = thislist[-1]
print(first_element)
print(last_element)

#How do you add an element to the end of a list?
thislist = [1 , 2 , 3 , 4 , 5]
thislist.append(6)
print(thislist)

#How do you insert an element at a specific position in a list?
thislist = [1 , 2 , 3 , 4 , 5]
thislist.insert(4,3)
print(thislist)

#How can you remove an element from a list by its value?
thislist = [1 , 2 , 3 , 4 , 5]
thislist.remove(3)
print(thislist)

#How do you create a new list that contains the squares of all elements in an existing list?
thislist = [1, 2, 3, 4, 5]
newlist = []
for i in thislist:
    square = i ** 2
    newlist.append(square)
print(newlist)

#second approch by syntax
thislist = [1, 2, 3, 4, 5]
newlist = [i ** 2 for i in thislist]
print(newlist)

#Write a list comprehension that filters out even numbers from a list of integers.
thislist = [1, 2, 3, 4, 5]
newlist = [i for i in thislist if i % 2 == 0]
print(newlist)

#How do you retrieve a sublist from a list in Python?
thislist = [1, [2, 3], 4, 5]
print(thislist[1 : 2])

#What does list[::-1] do?
thislist = [1, [2, 3], 4, 5]      #slicing syntax = [start:stop:step]
print(thislist[:: -1])

#How can you find the index of a specific element in a list?
thislist = [1, [2, 3], 4, 5]   
result = thislist.index([2, 3])
print(result)

#How do you count the number of occurrences of an element in a list?
thislist = [1, [2, 3], 4, 5, 3, 4, 4 , 4, 4]
result  = thislist.count(4)
print(result)

#What method would you use to sort a list in ascending 
#Print the list directly after sorting:
thislist = [1, 5, 6, 3, 6, 9, 1]   
thislist.sort()
print(thislist)

#Use the sorted() function, which returns a new sorted list:
thislist = [1, 5, 6, 3, 6, 9, 1]   
result = sorted(thislist)
print(result)

#What method would you use to sort a list in decending
thislist = [1, 5, 6, 3, 6, 9, 1]   
thislist.sort(reverse = True)
print(thislist)
