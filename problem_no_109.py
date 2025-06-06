# Given an integer array nums, return the most frequent even element. If there is a tie, return the smallest one. If there is no such element,
# return -1.
# Example 1:   Input: nums = [0,1,2,2,4,4,1]   Output: 2
# Explanation: The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most. We return the smallest one, which is 2.
# Example 2: Input: nums = [4,4,4,9,2,4]       Output: 4
# Explanation: 4 is the even element appears the most.
# Example 3: Input: nums = [29,47,21,41,13,37,25,7]    Output: -1
# Explanation: There is no even element.
# example 4 : input :nums = [8154,9139,8194,3346,5450,9190,133,8239,4606,8671,8412,629]  output :3346


nums = [8154,9139,8194,3346,5450,9190,133,8239,4606,8671,8412,6290]  #this example is tie in frequency,the smallest even number among those tied is stored in max_key.
temp = {}
for i in nums:
    if i not in temp:
        temp[i] = 1
    else:
        temp[i] += 1
#{8154: 1, 9139: 1, 8194: 1, 3346: 1, 5450: 1, 9190: 1,133: 1, 8239: 1, 4606: 1, 8671: 1, 8412: 1, 6290: 1}
max_appear_el = 0
max_key = -1
for key,value in temp.items():
    if key % 2 == 0:
        if (value > max_appear_el) or (value == max_appear_el and key < max_key):
            max_appear_el = value
            max_key = key
print(max_key)
#If the frequency of the current even number (value) is greater than max_appear_el, then update max_appear_el and set max_key to this number.
# If the current even number has the same frequency (value == max_appear_el), check if the number (key) is smaller than the current max_key.
# If it is, update max_key to this smaller number. This ensures that: Most frequent even number is stored in max_key.
# If there’s a tie in frequency, the smallest even number among those tied is stored in max_key.
            

        
            
