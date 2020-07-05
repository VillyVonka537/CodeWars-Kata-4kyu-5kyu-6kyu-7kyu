# The main idea is to count all the occurring characters in a string. If 
# you have a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object 
# literal, {}.

def count(string):
    counter = {}
    for char in string:
        counter[char] = counter.get(char, 0) + 1
    return counter
