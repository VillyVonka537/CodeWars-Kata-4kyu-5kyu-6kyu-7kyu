# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric 
#digits that occur more than once in the input string. The input string can be assumed to contain only alphabets
#(both uppercase and lowercase) and numeric digits.
# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'

def duplicate_count(text):
    text = text.lower()
    duplicates = []
    for item in text:
        if text.count(item) > 1 and item not in duplicates:
            duplicates.append(item)    
    return len(duplicates)
