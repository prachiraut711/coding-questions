n = 5
for i in range(n):
    for j in range(n - i):
        if  i== 0 or j == 0 or j == n - i - 1 :
            print("*", end = " ")
        else:
            print(" ",end = " ")
    print() 