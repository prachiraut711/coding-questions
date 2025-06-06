#print 1st non repating charcter in string

# s = "aabbcddefe"
# dict = {}
# for i in s:
#     if i not in dict:
#         dict[i] = 1
#     else:
#         dict[i] += 1
# print(dict)
# for i, j in dict.items():
#     if j == 1:
#         print(i)
#         break

# s = "aabbcddefe"
# for i in s:
#     if s.count(i) == 1:
#         print(i)
#         break

s = "aabbcddefe"
for i in range(len(s)):
    for j in range(i, len(s)):
        if i in j:
            print(i)

