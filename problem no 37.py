#give sum of cube of each digit in number .ex num=153 => (1)**3+(5)**3+(3)**3

num = str(input("Enter the number:"))
sum = 0
for i in num:
    sum += int(i) ** 3    #if i write(i ** 3)tar error yeil.ithe fakt jyala str kel tyala int karaych.
print(sum)


# num = 12345
# sum = 0
# while num:
#     r = num % 10
#     sum += r ** 3
#     num = num // 10
# print(sum)

