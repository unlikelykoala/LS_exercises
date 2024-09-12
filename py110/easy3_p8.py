'''
Input: 2 integers (count, start)
Output: list

Explicit:
    -  return a list containing the same number of elements as the count argument
    - start point is 2nd argument
    - all elements should be multiples of starting number
    - count will alwayu be >= 0
    - if count == 0, return empty list

Implicit:
    - in order

Questions:
    - 

Data structures:
    - 

Algorithm:
    1. check if count 0, if os return []
    2. create an empty list
    3. create inclusive range from 1 to count
    4. create an element for each element in range
        - multiple by range index
        - append to list
    5. return list
'''

def sequence(count, start):
    return [start * num for num in range(1, count+1)]

print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True
