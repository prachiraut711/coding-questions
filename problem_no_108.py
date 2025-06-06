# If given String is I_LOVE_INDIA reverse whole string except "_". Output for this would be A_IDNI_EVOLI

s = "I_LOVE_INDIA"
u = s[::-1]
l = []
for i in range(len(u)):
    if u[i].isalpha():   #u becomes the reverse of s, which is "AIDNI_EVOL_I" (this uses Python's slicing to reverse the string).
        l.append(u[i])   #l becomes ['A', 'I', 'D', 'N', 'I', 'E', 'V', 'O', 'L', 'I'].
for i in range(len(s)):
    if not s[i].isalpha():  #This loop goes through the original string s = "I_LOVE_INDIA".
        l.insert(i, s[i])   # For each position i where s[i] is not an alphabetic character (like underscores _), that non-alphabetic
p = ''.join(l)              # character is inserted back into the list l at position i.
print(p)                    # After this loop, l becomes ['A', '_', 'I', 'D', 'N', '_', 'I', 'E', 'V', '_', 'O', '_', 'L', 'I'].






