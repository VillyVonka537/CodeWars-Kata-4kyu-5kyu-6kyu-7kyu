# In this kata, you've to count lowercase letters in a given string 
# and return the letter count in a hash with 'letter' as key and count 
# as 'value'. The key must be 'symbol' instead of string in Ruby and 
# 'char' instead of string in Crystal.

def letter_count(s):
    return dict((item, s.count(item)) for item in sorted(set(s)))
