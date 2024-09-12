'''
Input: string
Output: string (double every char of input string)

Explicit:
    - double each char
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

def repeater(string1):
    return ''.join([char * 2 for char in string1])

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True
