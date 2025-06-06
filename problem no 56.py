n = 5
for i in range(0, n):
    for j in range(0, n - i - 1):
        print(" ", end = " ")
    for j in range(0, i + 1):
        print("*", end = " ")    #"* " ithe space dili mag diamond shape ala varcha nahitar right angle triangle disla asta
    print()
for i in range(0, n - 1):
    for j in range(i + 1):
        print(" ", end = " ")
    for k in range(0, n - i - 1):
        print("*", end = " ")
    print()