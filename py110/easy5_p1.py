'''
input: dict
output: dict with keys-values inverted

explicit rules:
- return new list
- include only transactions in first arg

implicit rules:
- 

questions:
- do i mutate or return a new dict?

data structures:
- dict

algorithm:
1. 

'''
def keep_keys(my_dict, keys):
    return {key: my_dict[key] for key in keys}

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys))# == expected_dict) # True
