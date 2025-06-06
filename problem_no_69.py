#How do you access elements in a tuple?
thistuple = ("apple",(2, 3) , 6, "hi")
result = thistuple[1]
print(result)

#to accesss inside nested tuple
thistuple = ("apple", (2, 3), 6, "hi")   #[1][0] ch output 2 yeil
print(thistuple[1][1])   #if i write print(thistuple([][]))tuple in tuple then it gives error

#Can you modify an element in a tuple? Why or why not?
#-> No, you cannot modify an element in a tuple. Tuples in Python are immutable, meaning that once a tuple is created, 
# its elements cannot be changed, added to, or removed.This immutability is a fundamental property of tuples.

#my_tuple = (1, 2, 3, 4)
#my_tuple[1] = 10               #GIVE ERROR...
#print(my_tuple)                #IT WILLL GIVE ERROR -> TypeError: 'tuple' object does not support item assignment.

#If you need to "modify" a tuple, you would typically create a new tuple with the desired modifications.
my_tuple = (1, 2, 3, 4)
new_tuple = my_tuple[:1] + (10,) + my_tuple[2:]
print(new_tuple)  # Output: (1, 10, 3, 4)

#How do you concatenate two tuples
tuple1 = (1, 2, 3)
tuple2 = (3, (4, 5), 10)
result = tuple1 +tuple2
print(result)

#What is tuple unpacking? Provide an example.
#->But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking"
my_tuple = ("apple", 2 ,"banana")
(red, yellow, green) = my_tuple
print(red)
print(yellow)
print(green)
#the number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

#How would you swap the values of two variables using a tuple?
my_tuple = ("apple", 2 ,"banana")
(red, yellow, green) = my_tuple
red,yellow = yellow,red
print(red)
print(yellow)

#approch2
my_tuple = ("apple", 2 ,"banana")
(red, yellow, green) = my_tuple
temp = red 
red = yellow
yellow = temp
print(red)
print(yellow)

#How can you count the occurrences of a specific element in a tuple?
my_tuple = ("apple", 2 ,"banana", 2, 2, 3, 2)
result = my_tuple.count(2)
print(result)

#How can you find the index of a specific element in a tuple?
my_tuple = ("apple", 2 ,"banana", 2, 2, 3, 2)
result = my_tuple.index("apple")
print(result)