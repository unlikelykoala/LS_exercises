'''
Input: list
Output: list (reversed by mutating it)

Explicit:
    - return a reversed list
    - must mutate it (returned object is the same object)
    - cannot use reverse method or slicing


Implicit:
    - empty list returns empty list

Questions:
    - 

Data structures:
    - list

Algorithm:
    1. create a copy of input list
    2. iterate over input list
        A: use copy to get values
        B: overwrite the input list using indexing
    return input list
'''

def reverse_list(lst):
    cpy_list = lst.copy()

    for idx in range(len(cpy_list)):
        lst[idx] = cpy_list[-idx-1]

    return lst


list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True
