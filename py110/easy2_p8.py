'''
Input: positive int
Output: list of digits in the input number

Explicit:
    - all ints are +

Implicit:
    - place digits in the order they appear

Questions:
    - 

Data structures:
    - list

Algorithm:
    1. Initialize empty list
    2. modulo by 10 = 1s digit
    3. prepend that digit to list
    4. int divide by 10
    5. return list

'''

def digit_list(num):
    lst = []

    while num:
        lst.insert(0, num % 10)
        num //= 10

    return lst


print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True
