'''
Input: list
Output: list composed of 2 lists
    1. 1st half of original list
    2. 2nd half of original list

Explicit:
    - 1st return vslure id 1st half of original list
    - 2nd return value is 2nd half of original list
    - if original list is odd, middle element goes in the first half

Implicit:
    - If only 1 ele, 2nd return val is empty list
    - empty list returns 2 empty lists

Questions:
    - should these be shallow or deep copies?

Data structures:
    - lists

Algorithm:
    1. Determine if length of list is odd or even
    2. Use slicing to return 1st half and 2nd half

'''

def halvsies(lst):
    half = (len(lst) + 1) // 2
    first_half = lst[:half]
    second_half = lst[half:]
    return [first_half, second_half]


# All of these examples should print True
print(halvsies([1, 2, 3, 4]))
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]))
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])
