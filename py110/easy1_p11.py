'''
Input: non-negative integer
Output: string representation of the integer

Explicit:
    - integer input will be non-negative
    - cannot use str or other conversion functions

Implicit:
    - unless 0, number is always signed

Questions:
    - does that mean that it could contain 0 words 
      or that it could 0 or more spaces?
    - what about initial zeros?
    - is the number always signed?

Data structures:
    - string
    - list

Algorithm:
    1. Determine if number is non-negativ
        A: if > 0, add '+' to num_str and proceed
        B: if < 0, add '-', mult by -1, and proceed
    2. Convert each digit to a character
        A: Initalize a list digit-chars
        B: Isolate each digit in integer
            - Get remainder after % 10
            - Reduce number by // 10
        C: Convert to char using the list
    2. Concatenate it to the string
    3. Return the string

'''
def signed_integer_to_string(num):
    num_str = ''

    if num < 0:
        sign = '-'
        num *= -1
    elif num > 0:
        sign = '+'
    else:
        sign = ''

    while num:
        digit = num % 10
        dig_str = num_list[digit]
        num_str = dig_str + num_str
        num //= 10
    
    num_str = sign + num_str
    return num_str or '0'

num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print(signed_integer_to_string(4321))
print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True
