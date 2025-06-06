# Python Program to Print all Prime Numbers in an Interval

for num in range(1,11):
    if num > 1 :
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(num)


# n = int(input())
# i = 2
# while i <= n:
#     flag = 0
#     for var in range(2,i):
#         if i % var == 0 :
#             flag = 1
#             break
#     if (flag == 0):
#         print(i)
#     i +=1