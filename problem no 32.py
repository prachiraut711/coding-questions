#find how many times a repeated  in string
# str = "aabbacdadee"
# rep_char = str.count("a") 
# print(rep_char)



#find first repeated charcter in string

str = "abbacdadee"
for char in str :
    if str.count(char) == 2 :
        print(char)
        break


       