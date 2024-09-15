'''
input: two lists
output: frozen set that is a combo of both lists

explicit rules:
- convert lists to frozen sets
- return frozen set that is a union of the frozen sets

implicit rules:
- 

questions:
- 

data structures:
- frozen set

algorithm:
1. convert lists to fs
2. unite fs
3. return frozen set

'''
def intersection(list1, list2):
    return frozenset(list1) & frozenset(list2)

list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})
print(intersection(list1, list2) == expected_result) # True
