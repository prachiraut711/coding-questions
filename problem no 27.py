#   sum of even numbers

num = int(input(" enter the number : "))
sum = 0
for i in range(num + 1):
    if i % 2 == 0 :
        sum += i
print(sum) 

# num = int(input(" enter the number : "))
# i = 1
# sum = 0
# while i <= num :
#     if i % 2 == 0:
#         sum += i
#     i += 1
# print(sum)