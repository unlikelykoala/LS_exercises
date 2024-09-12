'''
Input: positive int
Output: positive int (digits reversed)

Explicit:
    - reverse digits
    - 

Implicit:
    - 1 digit just return digit

Questions:
    - 

Data structures:
    - 

Algorithm:
    1. if 1 digit, return digit
    2. change to a string
    3. reverse the string
    4. change to an int
    5. return int
'''

def reverse_number(num):
    return int(str(num)[::-1])


print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True                           # True
