# Bubble sort
arr = [15, 16, 6, 8, 5]
for i in range(len(arr)- 1):
    flag = 0
    for j in range(len(arr) - 1 - i):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp
            flag = 1
    
    if flag == 0:
        break
print("Bubble sort :", arr)

