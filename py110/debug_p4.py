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
This returns an error because trying to access a non-existent will raise an exception.
This `if` block checks for truthiness; it doesn't catch exceptions.

'''
def get_key_value(my_dict, key):
    return my_dict.get(key, None)

print(get_key_value({"a": 1}, "b"))
