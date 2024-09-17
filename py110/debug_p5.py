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
def decrease(counter):
        return counter - 1

counter = 10

for _ in range(10):
    print(counter)
    counter = decrease(counter)

print('LAUNCH!')
