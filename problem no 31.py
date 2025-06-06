#find the first non repeated character

str = " aabbcddee "
for char in str :
    if str.count(char) == 1:
        print(char)
        break



