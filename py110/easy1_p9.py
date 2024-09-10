'''
Input: string of digits prefxed with + or -
Output: integer (same value as digits)

Explicit:
    - do not use standard conversion functions like int()
    - all input is valid numeric
    - string may have a leading + or - sign; 
        if the first character is a +, return a positive number; 
        if it is a -, return a negative number. 
        if there is no sign, return a positive number.

Implicit:

Questions:
    - can i use ord()?
    - what about empty strings?

Data structures:
    - 

Algorithm:
    1. Check if there's a sign.
    2. Return sum
'''
def string_to_signed_integer(num_str):
    if num_str[0].isdigit():
        return string_to_integer(num_str)
    elif num_str[0] == '+':
        return string_to_integer(num_str[1:])
    else:
        return -(string_to_integer(num_str[1:]))

def string_to_integer(num_str):
    sum = 0
    multiplier = 1

    for char in num_str[::-1]:
        num = (ord(char) - 48) * multiplier
        sum += num
        multiplier *= 10

    return sum


print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True

# def hexadecimal_to_integer(num_str):
#     num = int(num_str, 16)
#     print(f'Using base-16 with int function: {num}')

#     num2 = int('0x' + num_str, 0)
#     print(f'Using int function\'s guessing feature: {num2}')

#     hex_dict = {
#         'A': 10,
#         'B': 11,
#         'C': 12,
#         'D': 13,
#         'E': 14,
#         'F': 15,
#         '0': 0,
#         '1': 1,
#         '2': 2,
#         '3': 3,
#         '4': 4,
#         '5': 5,
#         '6': 6,
#         '7': 7,
#         '8': 8,
#         '9': 9,
#     }
    
#     num3 = 0

#     for char in num_str:
#         current_value = hex_dict[char.upper()]
#         num3 = (16 * num3) + current_value
        

#     print(f'Using a dictionary: {num3}')

# hexadecimal_to_integer('4D9f')


