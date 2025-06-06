# keep asking the user for input until they enter number between 1 to 10

# while True:
#     num = int(input("The number between 1 to 10 : "))
#     if 1 <= num <= 10:
#         continue
#     print(f"The {num} is not between 1 to 10")

while True:
    num = int(input("The number between 1 to 10 : "))
    if 1 <= num <= 10:
        print(f"The {num} is between 1 to 10")
        break
    else:
        print(f"The {num} is not between 1 to 10")