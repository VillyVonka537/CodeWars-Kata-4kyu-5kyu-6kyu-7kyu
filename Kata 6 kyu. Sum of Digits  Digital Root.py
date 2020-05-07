# In this kata, you must create a digital root function.
# A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. 
#If that value has more than one digit, continue reducing in this way until a single-digit number is produced. 
#This is only applicable to the natural numbers.
# Here's how it works:
# digital_root(16)
# => 1 + 6
# => 7

def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))