'''
Input: string
Output: string (double every consonant of input string)

Explicit:
    - double each consoant, not each char
    - 

Implicit:
    - empty string returns empty string

Questions:
    - 

Data structures:
    - 

Algorithm:
    1. Initalize empty string
    2. Iterate through input string
        A: concatenate each char twice to new string
    3. Return new string
'''

def double_consonants(string1):
    return ''.join([char * 2 
                    if char.casefold() in 'bcdfghjklmnpqrstvwxyz'
                    else char
                    for char in string1])

# All of these examples should print True
print(double_consonants('String'))
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")                          # True
