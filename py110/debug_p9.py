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
When `decrease` is called in each iteration of the `for` loop,
its return value is not assigned to a global variable, so the global `counter` 
is unaffected by the calls to`decrease` and thus remains `10`.

'''
import copy
data_set = {1, 2, 3, 4, 5}
new = copy.copy(data_set)
for item in data_set:
    if item % 2 != 0:
        new.remove(item)
print(new)
