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
def reverse_string(string):
    new = ''
    for char in string[::-1]:
        new += char

    return (new)
    # return (string[::-1])


reverse_string("hello")
