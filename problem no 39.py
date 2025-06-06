# check if all elements in string are unique.if duplicate is found the exit the loop and print the without duplicate .

str = "abcdabc"
dict = {}
result = ""
for char in str:
    if char in dict:
        break
    dict[char] = 1
    result += char
print(result)



# str = "abcdabc"
# result = ""
# for char in str:
#     if char in result:
#         break
#     result += char
# print(result)