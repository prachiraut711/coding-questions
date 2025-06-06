#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
# You are given  scores. Store them in a list and find the score of the runner-up.2 <= n >=10


# #approch1
n = int(input())
arr = list(map(int,input().split()))  #To make arr a list of integers, you would typically wrap the map object with list(), like so:
arr.sort(reverse = True)
max_element = arr[0]
for i in arr:
    if max_element > i:
        print(i)
        break

# #approch2
n = int(input())
arr = list(map(int,input().split()))
thisset = set(arr)
sorted_list = sorted(thisset, reverse=True)
print(sorted_list[1])

#approch3( O(n)complexity direct ekach traverse madhe  dil.interview question ahe)
n = int(input())
arr = list(map(int,input().split()))
first_max = float("-inf")
second_max = float("-inf")
for i in range(len(arr)):
    if arr[i] > first_max:
        second_max = first_max
        first_max = arr[i]
    elif arr[i] > second_max and arr[i] != first_max:
        second_max = arr[i]
print(second_max)




