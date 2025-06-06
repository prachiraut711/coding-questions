#Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. 
# Iterate through each command in order and perform the corresponding operation on your list.
N = int(input())
thislist = []
while N:
    com = input()             #ex : insert 0 1
    split = com.split()       #split ni ["insert"(index 0),"0"(index 1),"1"(index 2)]
    if split[0] == "insert":
        thislist.insert(int(split[1]),int(split[2]))   #ata he eka string madhe ahe aplyla 1 ani 2nd position ch insert karych mag ithe 0,1 he str madhe mag tyla int kel.
    elif split[0] == "print":
        print(thislist)
    elif split[0] == "pop":
        thislist.pop()
    elif split[0] == "reverse":
        thislist.reverse()
    elif split[0] == "remove":
        thislist.remove(int(split[1]))
    elif split[0] == "append":
        thislist.append(int(split[1]))
    else:
        thislist.sort()
    N -= 1