'''
input: list of strings
output: new list of same string without vowels

explicit rules:
- return new list
- same string in the list without vowels

implicit rules:
- multiple strings in list is possible

questions:
- 

data structures:
- list

algorithm:
1. Create a new list
2. Create new string in new list
3. Iterate through string
4. if not in vowels, add to the string
5. return the list

'''
VOWELS   = 'aeiou'

# def remove_vowels(lst):
#     new_lst = []
#     for ele in lst:
#         new_str = ''
#         for char in ele:
#             if char.casefold() not in VOWELS:
#                 new_str += char
#         new_lst.append(new_str)
#     return new_lst
def strip_vowels(string):
    no_vowels = [char for char in string
                 if char.casefold() not in VOWELS]
    return ''.join(no_vowels)

def remove_vowels(lst):
    return [strip_vowels(string) for string in lst]

# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True
