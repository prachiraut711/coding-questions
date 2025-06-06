#CONVERT DECIMAL TO BINARY.

n = int(input())   #ex 13 => 1101
ans = ""
while(n != 0):
    if(n % 2 == 1):
        ans += "1"
    else:
        ans += "0"
    n = n // 2 
rev_str = ans[::-1]
print(rev_str)


#CONVERT BINARY TO DECIAL.

num = 10
binary_val = num
decimal_val = 0
base = 1

while num > 0:
    rem = num % 10
    decimal_val = decimal_val + rem * base
    num = num // 10
    base = base * 2

print(f"Binary Number is {binary_val}\nDecimal Number is {decimal_val}")
