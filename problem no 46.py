# column = 5
# for i in range(1, column + 1):
#     for j in range(1, (column + 2) - i):
#         print("*", end = " ")
#     print()


rows = 5
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end = " ")
    print()