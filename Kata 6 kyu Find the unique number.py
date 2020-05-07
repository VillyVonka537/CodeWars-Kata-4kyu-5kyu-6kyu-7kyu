# There is an array with some numbers. All numbers are equal except for one. 
# Try to find it!

# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

# It’s guaranteed that array contains at least 3 numbers.
# The tests contain some very huge arrays, so think about performance.
# This is the first kata in series:

#     Find the unique number (this kata)
#     Find the unique string
#     Find The Unique

### 1st my solution, but Codewar server is timeout 12000ms 

### def find_uniq(arr):
###     y = [item for item in arr if arr.count(item) % 2 != 0 and arr.count(item) < 2]
###     for i in y:
###         return i

# 2d solution

def find_uniq(arr):
    arr1 = set(arr)
    for i in arr1:
        if arr.count(i) == 1:
            return i