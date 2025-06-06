# n = 5
# for i in range(0, n):
#     for j in range(i + 1, n):
#         print(" ", end = " ")
#     for k in range(0, i + 1):
#         print("*", end = " ")
#     for l in range(1, i + 1):
#         print("*", end = " ")
#     print()


n = 5
for i in range(0, n):
    for j in range(i + 1, n):
        print(" ", end = " ")
    for k in range(2 * i + 1):
        print("*", end = " ")
    print()