# print factors of number5

def print_factors(x):
    print("the factors of",x,"are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)
num = 320 
print_factors(num)    #ithe kahi return ch nahi dilay mg print nahia al


