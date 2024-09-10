'''
Input: string
Output: bool (True if input is palindrome, False if not)

Explicit: 
    - palindrome is word same forwards and backwards
    - case matters
    - all characters matter

Implicit:
    - drfg

Questions:
    - what does it mean that all characters matter? does that include spaces?

Data structure(s):
    - 

Algorithm:
    1. 
'''
def is_palindrome(input_str):
    return input_str == input_str[::-1]

# test cases # All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)
