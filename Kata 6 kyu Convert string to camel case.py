# Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
# The first word within the output should be capitalized only if the original word was capitalized
# (known as Upper Camel Case, also often referred to as Pascal case).
# Examples

#to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"
#to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"

def to_camel_case(text):
    new_text = text.replace('-', '_').split('_')
    for item in range(1, len(new_text)):
        new_text[item] = new_text[item].capitalize()
    return ''.join(new_text)