'''
Input: string
Output: bool (True if input is palindrome, False if not)

Explicit: 
    - palindrome is word same forwards and backwards
    - case-insensitive
    - ignore non-alphanumeric chars
    - all characters matter

Implicit:
    - remove non-alphanumerics

Questions:
    - what does it mean that all characters matter? does that include spaces?

Data structure(s):
    - 

Algorithm:
    1. REMOVE non-alphanumerics
    2. Make case-insensitive
    3. Check if palindrome
'''
def is_real_palindrome(s):
    alphanums_only = ''

    for char in s:
        if char.isalnum():
            alphanums_only += char.casefold()
    
    return alphanums_only == alphanums_only[::-1]

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True
