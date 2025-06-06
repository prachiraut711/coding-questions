# You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.
# For each index i, names[i] and heights[i] denote the name and height of the ith person.
# Return names sorted in descending order by the people's heights.
# Example 1:
# Input: names = ["Mary","John","Emma"], heights = [180,165,170]
# Output: ["Mary","Emma","John"]
# Explanation: Mary is the tallest, followed by Emma and John.
# Example 2:
# Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
# Output: ["Bob","Alice","Bob"]
# Explanation: The first Bob is the tallest, followed by Alice and the second Bob.

#****imp***The key parameter tells sorted() what to focus on when sorting. Let's break this part:Each item in mapped.items() is a tuple, e.g., ('Mary', 180).lambda item: item[1] means:For the tuple ('Mary', 180), the value 180 (at item[1]) will be used as the sorting key.For ('John', 165), it uses 165.For ('Emma', 170), it uses 170.

names = ["Mary","John","Emma"]
heights = [180,165,170]
zipped = list(zip(names, heights))
sorted_zipped = sorted(zipped, key=lambda item: item[1], reverse=True)
sorted_names = [name for name, height in sorted_zipped]
print(sorted_names)