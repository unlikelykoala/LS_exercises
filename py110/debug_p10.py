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
data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = []
for num in data:
    if num not in unique_data:
        unique_data.append(num) 
print(unique_data == [4, 2, 1, 3]) # order not guaranteed
