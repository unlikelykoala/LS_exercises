'''
Input: integer
Output: list

Explicit:
    - return list containing all numbers between 1 and argument inclusive
    - 

Implicit:
    - in order

Questions:
    - 

Data structures:
    - 

Algorithm:
    1. create an inclusive range starting from 1
    2. change it to a list
    3. return list
'''

def sequence(num):
    return list(range(1, num+1))

print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True
