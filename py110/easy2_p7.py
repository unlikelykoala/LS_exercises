'''
Input: 2 lists of numbers
Output: list (each ele is prod of eles from 2 lsts at same index)

Explicit:
    - same number of elements
    - numbers only

Implicit:
    - no empty lists

Questions:
    - 

Data structures:
    - list

Algorithm:
    1. Iterate through list1
        multiple elements of the same index and save prod in new list
    2. return new list of products

'''

def multiply_list(lst1, lst2):
    return [lst1[idx] * lst2[idx] for idx in range(len(lst1))]


list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True
