
n = int(input())
aadvapen = True

for i in range(2, n//2 + 1):
    if n % i == 0:
        aadvapen = False
        break

if aadvapen :
    print("prime")
else:
    print("Not-prime")