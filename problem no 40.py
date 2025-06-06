str = "abcdabac"
dict = {}

for char in str:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1

print(dict)