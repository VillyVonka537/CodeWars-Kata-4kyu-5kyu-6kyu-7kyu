#Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

#move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]

def move_zeros(array):
    new_array = []
    zer_array = []
    for item in array:
        if item != 0 or type(item) == bool :
            new_array.append(item)
        else:
            zer_array.append(item)
    new_array.extend(zer_array)
    return new_array
