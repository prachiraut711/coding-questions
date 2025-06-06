# count the vowels in sentence.

# sentence = (input("Enter the sentance:")) 
# sent_lower = sentence.lower()
l = ["a", "e", "i", "o", "u"]
# count = 0
# for char in list:
#     if char in sentence.lower():
#         count += 1
# print(count)

letter = 'welcome'
   
found = False
count = 0
for i in letter:
    for item in l:
        if item == i:
            found = True
            count += 1
            break 
print(count)




# found = False
# for item in l:
#     if item == letter:
#         found = True
#         break 
# if found:
#     print("The letter is in the list.")
# else:
#     print("The letter is not in the list.")