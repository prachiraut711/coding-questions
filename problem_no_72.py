#The included code stub will read an integer,n , from STDIN.
# Without using any string methods, try to print the following:123...n
# Note that "" represents the consecutive values in between.
# ex. n = 5 output= 12345

n = int(input())
for i in range(1, n + 1):
    print(i, end = "")

#OR
n = int(input())
numbers = ""
for i in range(1, n + 1):
    numbers = numbers + str(i)
print(numbers)