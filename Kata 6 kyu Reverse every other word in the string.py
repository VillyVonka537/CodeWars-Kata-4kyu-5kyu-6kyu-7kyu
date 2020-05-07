# Reverse every other word in a given string, then return the string. Throw away any leading or trailing whitespace, 
# while ensuring there is exactly one space between each word. Punctuation marks should be treated as if they are apart
# of the word in this kata.

def reverse_alternate(string):
  if string == "":
      return ""
  else:
      newArr = []
      for i in range(len(string.split())):
          if i%2 != 0:
              newArr.append(string.split()[i][::-1])
          else:
              newArr.append(string.split()[i])
      return " ".join(newArr)