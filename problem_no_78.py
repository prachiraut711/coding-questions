#3rd largest 

n = int(input())
arr = list(map(int,input().split()))
first_max = float("-inf")
second_max = float("-inf")
third_max = float("-inf")
for i in range(len(arr)):
    if arr[i] > first_max :
        third_max = second_max
        second_max = first_max
        first_max = arr[i]
    elif arr[i] > second_max and arr[i] != first_max:
        third_max = second_max
        second_max = arr[i]
    elif arr[i] > third_max and arr[i] != second_max:
        third_max = arr[i]
print(third_max)








