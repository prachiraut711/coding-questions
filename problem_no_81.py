# sum of digonal(means 1,5,9 chi sum)
def my_func(nested_list):
    sum = 0
    for i in range(len(nested_list)):
        for j in range(len(nested_list[i])):
            if i == j:
                sum += nested_list[i][j]
    print(sum)
nested_list = [[1,2,3], [4,5,6], [7,8,9]]
my_func(nested_list)

      
#sum of ulta diagonal(means 3, 5,7 chi sum)
def my_func(nested_list):
    sum = 0
    for i in range(len(nested_list)):
        for j in range(len(nested_list[i])):
            if j == len(nested_list) - 1 - i:
                sum += nested_list[i][j]
    print(sum)
nested_list = [[1,2,3], [4,5,6], [7,8,9]]
my_func(nested_list)

                  



        



