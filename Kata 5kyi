#Complete the greatestProduct method so that it'll find the greatest product of five consecutive digits in the given string of digits.
#For example:
#greatestProduct("123834539327238239583") // should return 3240
#The input string always has more than five digits.
#Adapted from Project Euler.


def greatest_product(n):
    l = [int(i) for i in n]
    product = []
    for i in range(len(l)-4):
       product.append(l[i] * l[i+1] * l[i+2] * l[i+3] * l[i+4])
    return sorted(product)[-1]
