'''
Input: string of digits
Output: integer (same value as digits)

Explicit:
    - do not use standard conversion functions like int()
    - all input is valid numeric

Implicit:

Questions:
    - can i use ord()?
    - what about empty strings?

Data structures:
    - 

Algorithm:
    1. Iterate through the string in reverse
        A: use ord() to get Unicode for each number
        B: Create a multiplier (multiply by 10 each iteration)
        C: Multiply ord value by multiplier
        D: Add to the sum
    2. Return sum
'''

def string_to_integer(num_str):
    sum = 0
    multiplier = 1

    for char in num_str[::-1]:
        num = (ord(char) - 48) * multiplier
        sum += num
        multiplier *= 10

    return sum

def hexadecimal_to_integer(num_str):
    num = int(num_str, 16)
    print(f'Using base-16 with int function: {num}')

    num2 = int('0x' + num_str, 0)
    print(f'Using int function\'s guessing feature: {num2}')

    hex_dict = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }
    
    num3 = 0

    for char in num_str:
        current_value = hex_dict[char.upper()]
        num3 = (16 * num3) + current_value
        

    print(f'Using a dictionary: {num3}')

hexadecimal_to_integer('4D9f')
#print(hexadecimal_to_integer('4D9f') == 19871)  # True
# print(string_to_integer("4321"))
# print(string_to_integer("4321") == 4321)  # True
# print(string_to_integer("570"))
# print(string_to_integer("570") == 570)    # True
