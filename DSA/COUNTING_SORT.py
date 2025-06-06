#counting sort

def counting_sort(arr):
    # Step 1: Find the maximum value
    max_element = 0
    for i in arr:
        if i > max_element:
            max_element = i

     # Step 2: Create a count array  and [0] it initaialize 0 in count like count = [0,0,0,0,0,0,0,0,0]  max_element + 1 means 9 here its range 0-9
    count = [0] * (max_element + 1)

    # Step 3: Count occurrences
    for i in arr:
        count[i] += 1

    # Step 4: Reconstruct the sorted array
    sorted_arr = []
    for i in range(len(count)):
        for _ in range(count[i]):    #the underscore (_) in for _ in range(count[i]) is a convention used to indicate that the loop variable is not important. It acts as a placeholder when you don't need to use the variable inside the loop.
            sorted_arr.append(i)     #jar _ yachya jagi j variablr vaprla asta tar 0,1,2 as range madhe append zal ast pn aplyalya 2 al tar 2,2 karyachay mahnun _ he vaprl
    
    return sorted_arr


arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Counting sort:",sorted_arr )