# You have an array of numbers.
# Your task is to sort ascending odd numbers but even numbers must be on their places.
# Zero isn't an odd number and you don't need to move it. If you have an empty array,
# you need to return it.

# Example
# sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
# sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]

def sort_array(source_array):
    new_arr = [x for x in source_array if x % 2 == 1]
    new_arr.sort()
    for item in range(len(source_array)):
        if source_array[item] % 2 == 0:
            new_arr.insert(item, source_array[item])
    return new_arr