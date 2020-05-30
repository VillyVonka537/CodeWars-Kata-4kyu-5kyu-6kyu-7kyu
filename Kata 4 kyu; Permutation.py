# In this kata you have to create all permutations of an input string and 
# remove duplicates, if present. This means, you have to shuffle all letters 
# from the input in all possible orders.

# Examples:

# permutations('a'); # ['a']
# permutations('ab'); # ['ab', 'ba']
# permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

# The order of the permutations doesn't matter.

def permutations(string):
    str_len = len(string)
    if str_len == 1: return [string]
    
    result = []
    for item, character in enumerate(string):
        temp_string = string[:item] + string[item+1:]   
        for permutation in permutations(temp_string):  
            result.append(character + permutation)
            
    result = list(set(result))  # remove dupl
    return sorted(result)