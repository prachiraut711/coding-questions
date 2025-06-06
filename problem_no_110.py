#Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.
# Example 1:  Input: s = "Hello World"       Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:  Input: s = "   fly me   to   the moon  "    Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3: Input: s = "luffy is still joyboy"    Output: 6
# Explanation: The last word is "joyboy" with length 6.

#APPROCH 1
s =  "   fly me   to   the moon  "
temp = s.split()
temp.reverse()
for i in temp:
    print(len(i))
    break

#APPROCH 2
s = "Hello World"
temp = s.split()
print(len(temp[len(temp)-1]))

#APPROCH 3
s = "luffy is still joyboy" 
temp = s.split()
print(len(temp[-1]))