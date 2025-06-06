# print second max diifernce

#perfect_soltion with O(n)
arr = [1, 4, 15, 10]
max_element = float("-inf")
second_max_element = float("-inf")
min_element = float("inf")
second_min_element = float("inf")
for i in arr:
    if i > max_element:
        second_max_element = max_element
        max_element = i
    elif i > second_max_element:
        second_max_element= i

    if i < min_element:
        second_min_element = min_element
        min_element = i
    elif i < second_min_element:
        second_min_element = i

result1 = max_element - second_min_element 
result2 = second_max_element - min_element
if result1 > result2:
    print(result1)
else:
    print(result2)



#time complexity: O(n^2)+O(n)+O(n) = O(n^2)+2 O(n) = O(n^2)
arr = [1, 4, 15, 10]
diff = []
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        diff.append(abs(arr[i]-arr[j]))

max_element = 0
second_max_elemrnt = 0

for i in diff:
    if i > max_element:
        max_element = i

for i in diff:
    if i > second_max_elemrnt and i != max_element:
        second_max_elemrnt = i
print(second_max_elemrnt)


# approch wiyh buit in methods
arr = [1, 4, 15, 10]
max_element = max(arr)
arr.remove(min(arr))
min_element = min(arr)
print(max_element - min_element)


