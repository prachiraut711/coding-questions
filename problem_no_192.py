nums = [-2, 0, -1]
max_product = 1
current_product = 1
for i in nums:
    current_product *= i
    max_product = max(max_product, current_product)
    if current_product < 0:
        current_product = 1
print(max_product)

