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

######################################################################################################################


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

# Task
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
    new2 = ''.join(str(i) for i in new) #в джоине идем по списку и каждую итерацию преобразовываем в str по списку и записываем все в строку
    new2 = int(new2)    #преобразовываем в int
    return new2

######################################################################################################################

# Find the first non-consecutive number
# 1454490% of 1,3683,461 of 9,718thecodeite
# Python
# TRAIN AGAINNEXT KATA
# Details
# Solutions
# Forks (11)
# Discourse (51)
# Collect|
# Your task is to find the first element of an array that is not consecutive.
# By not consecutive we mean not exactly 1 larger than the previous element of the array.
# E.g. If we have an array [1,2,3,4,6,7,8] then 1 then 2 then 3 then 4 are all consecutive but 6 is not, so that's the first non-consecutive number.
# If the whole array is consecutive then return null2.
# The array will always have at least 2 elements1 and all elements will be numbers. The numbers will also all be unique and in ascending order. The numbers could be positive or negative and the first non-consecutive could be either too!

def first_non_consecutive(a):
    i = a[0] 
    for e in a:
        if e != i:
            return e
        i += 1
    return None

######################################################################################################################

# Description:
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
# Task
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

# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
# Write a function which takes a list of strings and returns each line prepended by the correct number.
# The numbering starts at 1. The format is n: string. Notice the colon and space in between.

def number(lines):
    m = []
    for (i, j) in enumerate(lines):
        m.append("" + str(i+1) + ": " + str(j))
    return m

######################################################################################################################

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
