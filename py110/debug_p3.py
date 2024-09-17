'''
input: 
output: 

explicit rules:
- 
implicit rules:
- 

questions:
- 

data structures:
- 

algorithm:
1. 

explanation:
`item` is a local copy of the element in lst, not the object itself.
When we multiply `item` by 2, this is changing the local `item` but not the element in `lst`.
To mutate `lst`, we need to use indexing.

'''
def multiply_list(lst):
    new = lst.copy()
    for idx in range(len(new)):
        new[idx] *= 2
    return new
    # return [ele * 2 for ele in lst]

print(multiply_list([1, 2, 3]) == [2, 4, 6])
