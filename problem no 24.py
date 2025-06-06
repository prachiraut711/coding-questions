# check if list is palindrome or not

list = [1 , 2 , 3 , 2, 1]
copy_list = list.copy()
copy_list.reverse()
if copy_list == list:
    print("list is palindrome")
else:
    print("list is not palindrome") 