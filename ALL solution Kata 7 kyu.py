#Kata 7 kyu Mumbling

# This time no story, no theory. The examples below show you how to write function accum:
# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.

def accum(s):
    result = ""
    for index, item in enumerate(s):
        result += item*(index+1) + "-"
    return result.strip('-').title()

######################################################################################################################

#Kata 7 kyu Vowel Count

# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, and u as vowels for this Kata.
# The input string will only consist of lower case letters and/or spaces.

def getCount(word):
    vowels = 0
    for letter in word:
        if letter.isalpha():
            if letter.lower() in 'a, e, i, o, u':
                vowels += 1
    return vowels

######################################################################################################################

#Kata 7 kyu Jaden Casing Strings

# Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). 
# Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known
# for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, check out how
# contractions are expected to be in the example below.
# Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from 
# Jaden Smith, but they are not capitalized in the same way he originally typed them.
# Example:
# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

def to_jaden_case(string):
    string = string.split(' ')
    new_string = []
    for item in string:
        item = item.capitalize()
        new_string.append(item)
    return' '.join(new_string)

######################################################################################################################

#Kata 7 kyu Isograms

# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that
# determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. 
# Ignore letter case.
# isIsogram "Dermatoglyphics" == true
# isIsogram "aba" == false
# isIsogram "moOse" == false -- ignore letter case

import collections
def is_isogram(string):
    string = list(string.lower())
    result = [item for item, count in collections.Counter(string).items() if count > 1]
    if len(result) == 0:
        return True
    else:
        return False

######################################################################################################################

#Kata 7 kyu Square Every Digit

# Welcome. In this kata, you are asked to square every digit of a number.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
# Note: The function accepts an integer and returns an integer

def square_digits(num):
    num = str(num)
    result = ''
    for item in num:
        result += str(int(item)**2)
    return int(result)

######################################################################################################################

#Kata 7 kyu Descending Order

#Your task is to make a function that can take any non-negative integer as a argument and return it with its digits 
#in descending order. Essentially, rearrange the digits to create the highest possible number.

#Examples:
#Input: 21445 Output: 54421
#Input: 145263 Output: 654321
#Input: 123456789 Output: 987654321

def descending_order(num):
    num = sorted(list(str(num)), reverse= True)
    for item in num:
        item = int(item)
    return int(''.join(map(str, num)))

######################################################################################################################

# Kata 7 kyu Shortest Word

# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.

def find_short(s):
    s = s.split(' ')
    new_s = []
    for item in s:
        new_s.append(len(item))
    return min(new_s)

######################################################################################################################

# Kata 7 kyu Get the Middle Character

# You are going to be given a word. Your job is to return the middle character of the word. If the word's length
# is odd, return the middle character. If the word's length is even, return the middle 2 characters.
# #Examples:
# Kata.getMiddle("test") should return "es"
# Kata.getMiddle("testing") should return "t"
# Kata.getMiddle("middle") should return "dd"
# Kata.getMiddle("A") should return "A"
# #Input
# A word (string) of length 0 < str < 1000 (In javascript you may get slightly more than 1000 in some test cases 
# due to an error in the test cases). You do not need to test for this. This is only here to tell you that you do
# not need to worry about your solution timing out.
# #Output
# The middle character(s) of the word represented as a string.

def get_middle(s):
    x = int(len(s)/2)
    return s[x] if len(s)%2!=0 else s[x-1:x+1]


######################################################################################################################

# Kata 7kyu Sum of odd numbers

#Given the triangle of consecutive odd numbers:
#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
# Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

# row_sum_odd_numbers(1); # 1
# row_sum_odd_numbers(2); # 3 + 5 = 8

def row_sum_odd_numbers(n):
    if type(n)==int and n>0:
        return n**3
    else:
        return "Input a positive integer"

#or

def row_sum_odd_numbers(n):
    return n**3

######################################################################################################################

# Kata 7kyu Highest and Lowest

# In this little assignment you are given a string of space separated numbers, and have to return the highest
# and lowest number.
# Example:
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"

def high_and_low(numbers):
    new_numbers = list(map(int, (numbers.split(' '))))
    min_num = str(min(new_numbers))
    max_num = str(max(new_numbers))
    result = ''.join(max_num + ' ' + min_num)
    return result

######################################################################################################################

# Kata 7kyu Hex Word Sum

# As hex values can include letters A through to F, certain English words can be spelled out, such as CAFE, BEEF, or FACADE. 
# This vocabulary can be extended by using numbers to represent other letters, such as 5EAF00D, or DEC0DE5.
# Given a string, your task is to return the decimal sum of all words in the string that can be interpreted as such hex values.
# Example
# Working with the string BAG OF BEES:
# BAG ==> 0 as it is not a valid hex value

def hex_word_sum(s):
  return sum(int(x, 16) for x in s.replace('O', '0').replace('S', '5').split() if all(y in '0123456789ABCDEF' for y in x))

######################################################################################################################

# Kata 7kyu Ordered Count of Characters

# Count the number of occurrences of each character and return it as a list of tuples in order of appearance.
# Example:

def ordered_count(input):
    return [(x, input.count(x)) for x in sorted(set(input), key=input.index)]

######################################################################################################################

# Kata 7kyu Love vs friendship

# If　a = 1, b = 2, c = 3 ... z = 26
# Then l + o + v + e = 54
# and f + r + i + e + n + d + s + h + i + p = 108
# So friendship is twice stronger than love :-)
# The input will always be in lowercase and never be empty.
#test.assert_equals(words_to_marks('attitude'), 100)

def words_to_marks(s):
    base = ord('a') - 1
    return sum(ord(l) - base for l in s)

######################################################################################################################

# Kata 7kyu Product Of Maximums Of Array (Array Series #2) 

# Introduction and Warm-up (Highly recommended)
# Playing With Lists/Arrays Series
# Task
# Given an array/list [] of integers , Find the product of the k maximal numbers.
# Notes
# Array/list size is at least 3 .
# Array/list's numbers Will be mixture of positives , negatives and zeros
# Repetition of numbers in the array/list could occur.
# Input >> Output Examples
# maxProduct ({4, 3, 5}, 2) ==>  return (20)

def max_product(lst, n_largest_elements):
    dCtver1 = sorted(lst,reverse=True)
    dCtver2 = dCtver1[0:n_largest_elements]
    n_largest_elements = 1
    for i in dCtver2:
        n_largest_elements *= i
    return n_largest_elements


######################################################################################################################

# Kata 7kyu Form The Largest 
# Given a number , Return _The Maximum number _ could be formed from the digits of the number given .
# Notes
# Only Natural numbers passed to the function , numbers Contain digits [0:9] inclusive !alt !alt
# Digit Duplications could occur , So also consider it when forming the Largest !alt
# Input >> Output Examples:
# maxNumber (213) ==> return (321)

def max_number(n):
    return int(''.join(sorted(str(n), reverse=True)))

# solution in details
def max_number(n):
    new = str(n)    #меняем тип
    new = list(map(int, new)) #преобразовываем строку в список чисел
    new = sorted(new, reverse=True) #сортируем по убывани (впринципе задача решена)
    new2 = ''.join(str(i) for i in new) #в джоине идем по списку и каждую итерацию преобразовываем в str по списку 
    #и записываем все в строку
    new2 = int(new2)    #преобразовываем в int
    return new2

######################################################################################################################

# Kata 7kyu Exclamation marks series #3: Remove all exclamation marks from sentence except at the 
# Remove all exclamation marks from sentence except at the end.
# Examples
# remove("Hi!") == "Hi!"
# remove("Hi!!!") == "Hi!!!"
# remove("!Hi") == "Hi"
# remove("!Hi!") == "Hi!"
# remove("Hi! Hi!") == "Hi Hi!"
# remove("Hi") == "Hi"

def remove(s):
    stripped = s.rstrip("!")
    newS = s.replace("!", "")
    outLen = len(s) - len(stripped)
    count = "!"*outLen
    newS += count
    return newS

######################################################################################################################

# Kata 7kyu Simple Fun #68: Palindrome Rearranging
# Given a string s, find out if its characters can be rearranged to form a palindrome.
# Example
# For s = "aabb", the output should be true.
# We can rearrange "aabb" to make "abba", which is a palindrome.
# Input/Output
# [input] string s
# A string consisting of lowercase English letters.

def palindrome_rearranging(s):
    count = 0
    for i in set(s):
        if s.count(i) % 2 != 0:
            count += 1
    if count > 1:
        return False
    else:
        return True

######################################################################################################################

# Kata 7kyu Pandemia 🌡️

# ⚠️ The world is in quarantine! There is a new pandemia that struggles mankind. 
# Each continent is isolated from each other but infected people have spread before the warning. ⚠️
# 🗺️ You would be given a map of the world in a type of string:
# string s = "01000000X000X011X0X"
# '0' : uninfected
# '1' : infected
# 'X' : ocean⚠️ 

def infected(s):
    lands = s.split('X')
    total = sum(map(len, lands))
    infected = sum(len(x) for x in lands if '1' in x)
    return infected * 100 / (total or 1)

######################################################################################################################

# Kata 7kyu Testing 1-2-3

# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
# Write a function which takes a list of strings and returns each line prepended by the correct number.
# The numbering starts at 1. The format is n: string. Notice the colon and space in between.

def number(lines):
    m = []
    for (i, j) in enumerate(lines):
        m.append("" + str(i+1) + ": " + str(j))
    return m

######################################################################################################################

# Kata 7kyu Two Oldest Ages

# The two oldest ages function/method needs to be completed. It should take an array of numbers as its argument and return the
# two highest numbers within the array. The returned value should be an array in the format [second oldest age, oldest age].
# The order of the numbers passed in could be any order. The array will always include at least 2 items.

def two_oldest_ages(ages):

    n = max(ages)
    ages.remove(n)
    m = max(ages)
    a = []
    a.append(n)
    a.append(m)
    a.sort()
    return a

######################################################################################################################

# Kata 7kyu Remove duplicate words

# Your task is to remove all duplicate words from a string, leaving only single (first) words entries.
# Example:
# Input:
# 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
# Output:
# 'alpha beta gamma delta'

def remove_duplicate_words(s):
    y = s.split()
    z = list()
    for i in y:
        if i not in z:
            z.append(i)
    return " ".join(z)

######################################################################################################################

# Kata 7kyu Simple letter removal

#In this Kata, you will be given a lower case string and your task will be to remove k characters from 
#that string using the following rule:
#For example: 
#solve('abracadabra', 1) = 'bracadabra' # remove the leftmost 'a'.
#solve('abracadabra', 2) = 'brcadabra'  # remove 2 'a' from the left.
#solve('abracadabra', 6) = 'rcdbr'      # remove 5 'a', remove 1 'b' 

def solve(st,k): 
    for letter in sorted(st)[:k]:
        st = st.replace(letter,'',1)
    return st
