#Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#Example 1:  Input: haystack = "sadbutsad", needle = "sad"  Output: 0
# Explanation: "sad" occurs at index 0 and  The first occurrence is at index 0, so we return 0.
# Example 2: Input: haystack = "leetcode", needle = "leeto"  Output: -1  Explanation: "leeto" did not occur in "leetcode", so we return -1.
 
haystack = "sadbutsad"
needle = "sad"
if needle in haystack:
    for i in range(len(haystack) - len(needle) + 1):  # Adjust loop to allow full comparison
        match = True
        for j in range(len(needle)):
            if haystack[i + j] != needle[j]:
                match = False
                break
        if match:
            print(i)  # Print the first occurrence index
            break  # Exit the loop after finding the first occurrence
else:
    print(-1)

#approch 2
haystack = "hello"
needle = "ll"
if needle in haystack:
    for i in range(len(haystack) - len(needle) + 1):  # Loop until there's enough room for needle
        if haystack[i:i + len(needle)] == needle:  # Check if substring matches needle
            print(i)  # Print the first occurrence index
            break  # Exit the loop after finding the first occurrence
else:
    print(-1)



#FOE APPROCH 1 :::>
# Let's say:
# haystack = "sadbutsad" (length = 9)
# needle = "sad" (length = 3)
# If you use for i in range(len(haystack) - len(needle) + 1):
# range(9 - 3 + 1) = range(7), so i will take values from 0 to 6.
# This means:
# At i = 0, you compare haystack[0:3] ("sad") with needle ("sad").
# At i = 1, you compare haystack[1:4] ("adb") with needle ("sad").
# ...
# At i = 6, you compare haystack[6:9] ("sad") with needle ("sad").
# Without the +1, the loop would only go up to i = 5, and you'd miss the last comparison at i = 6.