'''
input: two lists
output: set that is a combo of both lists

explicit rules:
- convert lists to sets
- return set that is a union of the sets

implicit rules:
- 

questions:
- 

data structures:
- set

algorithm:
1. convert sets
2. unite sets
3. return set

'''
def merge_sets(list1, list2):
    return set(list1) | set(list2)

list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# Prints True
