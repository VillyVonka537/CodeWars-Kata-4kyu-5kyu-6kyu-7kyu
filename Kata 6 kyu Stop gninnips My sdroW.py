# Write a function that takes in a string of one or more words, and 
# returns the same string, but with all five or more letter words 
# reversed (Just like the name of this Kata). Strings passed in will 
# consist of only letters and spaces. Spaces will be included only when 
# ore than one word is present.

# Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
# spinWords( "This is a test") => returns "This is a test" 
# spinWords( "This is another test" )=> returns "This is rehtona test"

def spin_words(chars):
    output = []
    for word in chars.split(' '):
        if len(word) > 4:
            word = word[::-1]
        output.append(word)
    return ' '.join(output)