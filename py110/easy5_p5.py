'''
input: 2 lists of ints (same length)
output: list (each ele is product of corresponding eles in other lists)

explicit rules:
- return new list
- mulitply correponding ele in each list for new ele

implicit rules:
- 

questions:
-what about empty lists/

data structures:
- list

algorithm:
1. iterate through both lists
    - zip
    - iterate through zip
        - multiply
        - add to new list
2. multiply corresponding elements
3. append the product to new list
4. return new list

'''
def multiply_items(list1, list2):
    return [num1 * num2 for num1, num2 in zip(list1, list2)]

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True
