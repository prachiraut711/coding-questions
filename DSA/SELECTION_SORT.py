# Selection Sort
arr = [7, 4, 10, 8, 3, 1]
for i in range(len(arr) - 1):
    min = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min]:
            min = j
    if min != i:
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp
print("Selection sort: ",arr)