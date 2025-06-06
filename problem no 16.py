#Python Program to Check Prime Number
n = int(input(("enter the no:")))
isPrime = True  # consider n is prime create variable ani tyala true getl mahnje its prime consider kel

for i in range(2, n//2 + 1):   #n/2 ni float yetay error yetoy mahnun floor division kel,jo number ahe tyala half kel ani tyatl ch divide kartat
    if n % i == 0:
        isPrime = False  #jithe if chi condition false zali ithe isPrime la false kel
        break

if isPrime:
    print("Prime")
else:
    print("Not prime")
    