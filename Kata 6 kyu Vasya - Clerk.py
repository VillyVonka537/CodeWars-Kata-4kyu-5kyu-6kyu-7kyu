# The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a 
# huge line. Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.
# Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.
# Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly 
# in the order people queue?
# Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment.
# Otherwise return NO.
# Examples:
# tickets([25, 25, 50]) # => YES 
# tickets([25, 100]) # => NO. Vasya will not have enough money to give change to 100 dollars

def tickets(people):
    tick25 = 0
    tick50 = 0
    tick100 = 0
    for tick in people:
        if tick == 25:
            tick25 += 1
        elif tick == 50:
            tick50 += 1
            if tick25 == 0:
                return "NO"
            tick25 -= 1
        elif tick == 100:
            tick100 += 1
            if tick50 > 0 and tick25 > 0:
                tick50-=1
                tick25-=1
            elif tick25 >= 3:
                tick25 = tick25-3
            else:
                return "NO"
    return "YES"
