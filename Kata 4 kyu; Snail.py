# Snail Sort

# Given an n x n array, return the array elements arranged from outermost 
# elements to the middle element, traveling clockwise.

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]

# For better understanding, please follow the numbers of the next array 
# consecutively:

# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]

# NOTE: The idea is not sort the elements from the lowest value to the 
# highest; the idea is to traverse the 2-d array in a clockwise 
# snailshell pattern.

# NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside 
# an array [[]].

def _snail(array):
    num = len(array)
    for item in range(0, (num + 1) // 2):
        new_item = num - 1 - item
        for j in range(item, new_item + 1):
            yield array[item][j]
        for i in range(item + 1, new_item + 1):
            yield array[i][new_item]
        for j in range(new_item - 1, item - 1, -1):
            yield array[new_item][j]
        for i in range(new_item - 1, item, -1):
            yield array[i][item]

def snail(array):
    return list(_snail(array)) if array and array[0] else []