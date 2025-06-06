# check if all elements in list are unique.if duplicate is found the exit the loop and print the without duplicate 

list = ["apple", "banana", "watermelon", "apple","banana" ,"cheeku"]

Table_list = []
Bag_list = []

for i in list:
    if i not in Bag_list:
        Bag_list.append(i)
    if i in Bag_list and i not in Table_list:
        Table_list.append(i)
    if i in Bag_list and i in Table_list:
        Bag_list.append(i)

print(Table_list)


        





