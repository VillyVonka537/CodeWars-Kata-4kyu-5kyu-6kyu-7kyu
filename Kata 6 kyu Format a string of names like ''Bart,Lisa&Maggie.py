# Given: an array containing hashes of names

# Return: a string formatted as a list of names separated by commas except for 
# the last two names, which should be separated by an ampersand.

# Example:
# list([ {name: 'Bart'}, {name: 'Lisa'}, {name: 'Maggie'} ])
# # returns 'Bart, Lisa & Maggie'
# list([ {name: 'Bart'}, {name: 'Lisa'} ])
# # returns 'Bart & Lisa'
# list([ {name: 'Bart'} ])
# # returns 'Bart'
# list([])
# # returns ''

# Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.

def namelist(names):
    if len(names) == 0: return ''
    elif len(names) == 1: return names[0]['name']
    return ', '.join([item['name'] for item in names[:-1]]) + ' & ' + names[-1]['name']