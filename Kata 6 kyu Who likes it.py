# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. 
# We want to create the text that should be displayed next to such an item.
# Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who
#  like an item. It must return the display text as shown in the examples:
# likes [] // must be "no one likes this"
# likes ["Peter"] // must be "Peter likes this"

def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return "{} likes this".format(names[0])
    elif len(names) == 2:
        return "{} and {} like this".format(names[0], names[1])
    elif len(names) == 3:
        return "{}, {} and {} like this".format(names[0], names[1], names[2])
    else:
        return "{}, {} and {} others like this".format(names[0], names[1], len(names)-2)