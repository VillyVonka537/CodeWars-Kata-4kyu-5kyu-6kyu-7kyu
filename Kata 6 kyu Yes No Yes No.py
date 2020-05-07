# Write a code that receives an array of numbers or strings, goes one by one through it while taking one value out, 
# leaving one value in, taking, leaving, and back again to the beginning until all values are out.
# It's like a circle of people who decide that every second person will leave it, until the last person is there. 
# So if the last element of the array is taken, the first element that's still there, will stay.
# The code returns a new re-arranged array with the taken values by their order. The first value of the initial 
# array is always taken.
# Examples:
# var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#  // returns [1, 3, 5, 7, 9, 2, 6, 10, 8, 4]

def yes_no(arr):
    new_arr = []
    for idx, num in enumerate(arr):
        if idx %2 == 0: 
            new_arr.append(num)
        else:
            arr.append(num)
    return new_arr