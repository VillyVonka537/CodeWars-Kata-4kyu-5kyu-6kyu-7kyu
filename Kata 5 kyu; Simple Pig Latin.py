Kata 5 kyu Simple Pig Latin.py
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    new_text = []
    for item in text.split(' '):
        if item.isalpha():
            new_item = item + item[0] + 'ay'
            new_text.append(new_item[1:])
        else:
            new_text.append(item)
    return ' '.join(new_text)
