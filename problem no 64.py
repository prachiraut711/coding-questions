# print prime numbers betweeen 1 to 10

for i in range(1, 11):
    if i > 1:  
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
