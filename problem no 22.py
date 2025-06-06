#Python Program to Find the Sum of Natural Numbers

n = int(input("enter the number:"))
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)