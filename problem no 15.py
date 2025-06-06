#Python Program to Find the Largest Among Three Numbers

a = int(input("enter 1st no:"))
b = int(input("enter 2nd no:"))
c = int(input("enter 3rd no:"))

if a >= b and a >= c:
    print(f"{a} is largest")
elif b >= a and b >= c :
    print(f"{b} is largest")
else:
    print(f"{c} is largest")