# Given an array, find the integer that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

# 1st Solution:

# def find_it(seq):
#     for i in seq:
#         if seq.count(i)%2!=0:
#             return i

def find_it(seq):
    new_seq = []
    for item in seq:
        item_count = seq.count(item)
        if item_count % 2:
            new_seq.append(str(item))
            return int(''.join(new_seq))
