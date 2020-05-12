# A pangram is a sentence that contains every single letter of the 
#alphabet at least once. For example, the sentence 
# "The quick brown fox jumps over the lazy dog" is a pangram, 
#because it uses the letters A-Z at least once (case is irrelevant).
# Given a string, detect whether or not it is a pangram. Return 
#True if it is, False if not. Ignore numbers and punctuation.

def is_pangram(s):
    result = ''.join(set(s.lower()))
    new_result = ''
    for item in result:
        if item.isalpha():
            new_result += item
    if len(new_result) == 26:
        return True
    else:
        return False