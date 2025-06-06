# rows = int(input("enter the number of rows:"))
# columns = int(input("enter the number of columns:"))
# symbol = input("enter the symbol:")

# for x in range(rows):
#     for y in range(columns):
#         print(symbol, end="")     #end="" used to not go on new line.
#     print(symbol)

# nested loops

# i = 1
# while i < 5:
#     j = 1
#     while j < 5:
#         print(j)
#         j += 1
#     i += 1
#     print()            #print()for new line.

# #    OR

for i in range(1, 5):
    for j in range(1, 5):
        print(j)
    print()