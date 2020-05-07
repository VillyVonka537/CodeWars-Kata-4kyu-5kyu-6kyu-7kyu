#In this simple Kata your task is to create a function that turns a string into a Mexican Wave. 
#You will be passed a string and you must return that string in an array where an uppercase letter 
#is a person standing up.
#Rules
#1.  The input string will always be lower case but maybe empty.
#2.  If the character in the string is whitespace then pass over it as if it was an empty seat.
#Example

#wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]

def wave(people):
    new_people = list(people)
    wave = []
    for item in range(len(new_people)):
        if people[item] != ' ':
            new_people[item] = new_people[item].capitalize()
            wave.append(people[:item] + new_people[item]+people[item+1:])
    return wave