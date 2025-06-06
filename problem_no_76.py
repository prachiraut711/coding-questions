# Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . 
# Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . 
# Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.
# n = sum nahi ali pahije

def approch_1(x, y, z, n):
    ans = []
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if (i + j + k != n):
                    ans.append([i, j, k])
    print(ans)

def approch_2(x, y, z, n):
    coordinate = [[i,j,k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n] #by list comphrension
    print(coordinate)

# Inputs
x = 1 
y = 1
z = 2
n = 3  

# function call
approch_1(x, y, z, n)
approch_2(x, y, z, n)