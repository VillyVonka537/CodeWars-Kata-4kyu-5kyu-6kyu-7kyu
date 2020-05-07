# You have function one_two (oneTwo for Java) that returns 1 or 2 with 50% chance. one_two is already defined in a global 
#scope and can be called everywhere.
# Your goal is to create function one_two_three (oneTwoThree for Java) that returns 1, 2 or 3 with equal probability 
#using only one_two function.
# Do not try to cheat returning repeating non-random sequences. There is randomness test especially for this case.

def one_two_three():
    r = one_two() * 3 + one_two()
    return 1 if r == 4 else 2 if r == 5 else 3 if r == 7 else one_two_three()