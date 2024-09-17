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
def append_to_list(value, lst=None):
    if not lst:
        lst = []
    lst.append(value)
    return lst

print(append_to_list(1) == [1])
print(append_to_list(2) == [2])
