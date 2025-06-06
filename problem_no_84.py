def my_func1(str):
    for i in str:
        if i in str.upper():
            print(i.lower(), end = "")
        else:
            print(i.upper(), end ="")
    print()            #end =''mule khalchyach pn output pudech yetay mahnun print()getl jayne ki new line var print hoil.
str = "PrAcHi"
my_func1(str)


def my_func2(str):
    ans = ""
    for i in str:     #this is correct approch than 1st.
        if i.isupper():
            ans += i.lower()   # he i.lower() ans empty string madhe append kel
        else:
            ans += i.upper()
    return ans

str = "PrAcHi"
result = my_func2(str)
print(result)



