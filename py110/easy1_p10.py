'''
Input: non-negative integer
Output: string representation of the integer

Explicit:
    - integer input will be non-negative
    - cannot use str or other conversion functions

Implicit:

Questions:
    - does that mean that it could contain 0 words 
      or that it could 0 or more spaces?
    - what about initial zeros?

Data structures:
    - string
    - list

Algorithm:
    1. Convert each digit to a character
        A: Initalize a dict of int-char pairs
        B: Isolate each digit in integer
            - Get remainder after % 10
            - Reduce number by // 10
        C: Convert to char using the dict
    2. Concatenate it to the string
    3. Return the string

'''

def integer_to_string(num):
    if num == 0: return '0'
    
    num_str = ''

    while num:
        digit = num % 10
        dig_str = num_dict[digit]
        num_str = dig_str + num_str
        num //= 10
    
    return num_str

num_dict = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
}

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True
