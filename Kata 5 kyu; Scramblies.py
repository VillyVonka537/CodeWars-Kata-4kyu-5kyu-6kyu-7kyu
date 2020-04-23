#Complete the function scramble(str1, str2) that returns true if a portion of str1 characters
#can be rearranged to match str2, otherwise returns false.

#Notes:

#Only lower case letters will be used (a-z). No punctuation or digits will be included.
#Performance needs to be considered
#Input strings s1 and s2 are null terminated.
#Examples
#scramble('rkqodlw', 'world') ==> True
#scramble('cedewaraaossoqqyt', 'codewars') ==> True
#scramble('katas', 'steak') ==> False


def scramble(s1,s2):
    for item in set(s2):
        if s1.count(item) < s2.count(item):
            return False
    return True
