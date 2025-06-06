#Insertion Sort
arr = [5, 4, 10, 1, 6, 2]
for i in range(1, len(arr)):
    temp = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > temp:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = temp
print("Insertion sort :", arr)