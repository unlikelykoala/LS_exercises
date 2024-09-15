'''
input: dict
output: list of keys, sorted by dict value

explicit rules:
- return a list of keys
- sorted by dict values

implicit rules:
- 

questions:
- 

data structures:
- list
- dict view object

algorithm:
1. get list of keys
2. sort based on value in dict
3. return lst

'''
def get_value(kv_pair):
    return kv_pair[1]

def order_by_value(dictionary):
    sorted_kvp = sorted(dictionary.items(), key=get_value)
    return [item[0] for item in sorted_kvp]

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True
