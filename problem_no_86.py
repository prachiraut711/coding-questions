#this is a string  is input and this-is-a-stringit is ouput .by using split and join

def my_func(x):
    x = line.split()
    result = "-".join(x)
    print(result)
line = input()
my_func(line)

#approch 2 (WITHOUT USING JOIN)
str = input()
ans = ""
for i in str:
    if i == " ":   #mahnje pahila whitespace bhetla tar thithe hypen append kel.(ithe " "ya madhe space de karan 1 space ahe input str madhe nahi dil tar tashich str print hoil.)
        ans += "-"
    else:
        ans += i  #mahnje ithe sagle letter add hotil ani varti missing space ala ki hypen add kelaay.
print(ans)


#approch3
def split_and_join(line):
    line = line.split()
    result = "-".join(line)
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

    