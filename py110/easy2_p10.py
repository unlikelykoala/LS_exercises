'''
Input: list of pos ints
Output: integer (avg of all elements rounded down)

Explicit:
    - all ints are +
    - no empty lists

Implicit:
    - 

Questions:
    - 

Data structures:
    - 

Algorithm:
    1. Sum all elements
    2. Integer division by length

'''

def average(lst):
    return sum(lst) // len(lst)


print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True
