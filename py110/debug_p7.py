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
This program redefines the built-in equation `sum`, but then tries to call the original built-in definition
within the function. However, that original definition has been lost.
They should rename the new function so it doesn't shadow the built-in function.

'''
def mult_sum(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(mult_sum(numbers, 2) == 20)
