'''
Input: two lists
Output: list with elements from two lists alternating

Explicit:
    - lists are same length
    - lists are not empty

Implicit:
    - start with first list

Questions:
    - 

Data structures:
    - list

Algorithm:
    1. zip the lists
    2. 

'''

# def interleave(lst1, lst2):
#     combined = []

#     for idx in range(len(lst1)):
#         combined.extend([lst1[idx], lst2[idx]])
    
#     return combined

def interleave(lst1, lst2):
    zipped = list(zip(lst1, lst2))

    combined = []

    for ele in zipped:
        combined.extend(ele)

    return combined


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True
