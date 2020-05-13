# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!

# Here's the deal:

#     It must start with a hashtag (#).
#     All words must have their first letter capitalized.
#     If the final result is longer than 140 chars it must return false.
#     If the input or the result is an empty string it must return false.

# Examples

# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "                  =>  "#HelloWorld"
# ""                                        =>  false

#optimize solution:

def generate_hashtag(words):
    output = "#"
    
    for word in words.split():
        output += word.capitalize()
    
    return False if (len(words) == 0 or len(output) > 140) else output

#test solution:

def generate_hashtag(words):
    hash = '#'
    if len(words) == 0 or len(words) > 140:
        return False
    elif len(words.split()) == 1:
        word_split = ''.join(words.split())
        return hash+word_split
    res_words = hash + ' ' + words
    print(res_words, "<<res_words>>")
    res_words = res_words.split()
    solution = []
    for item in res_words:
        item = item.capitalize()
        # print(item, "<<item>>")
        solution.append(item)
    solution = ''.join(solution)
    return solution