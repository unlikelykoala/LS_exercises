'''
input: two lists
output: set that is items unique to first list

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
1. convert to sets
2. difference
3. return set

'''
def unique_from_first(list1, list2):
    return set(list1) - set(list2)

list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})
