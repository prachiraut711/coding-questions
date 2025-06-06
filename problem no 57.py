n = 5
for i in range(n):
    for j in range(n):
        if j == 0 or j == n - 1:     #Ithe j= 0ani j=4 asel tar square madhun shevtche yetayet
            print("*", end = " ")
        else:
            print("", end = " ")
    print()