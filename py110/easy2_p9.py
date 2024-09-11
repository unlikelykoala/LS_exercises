'''
Input: list
Output: string with value of mult. avg. rounded to 3 dec

Explicit:
    - print "element => count"
    - case-sensitive

Implicit:
    - no empty lists

Questions:
    - no empty lists?
    - always strings?

Data structures:
    - dict

Algorithm:
    1. Initialize empty dict
    2. iterate through list
        - if ele not in dict, init to 0
        - increment by 1
    3. iterate through dict
        - print each kvp

'''

def count_occurrences(lst):
    dict1 = {}

    for ele in lst:
        dict1[ele] = dict1.get(ele, 0) + 1
    
    for key, value in dict1.items():
        print(f'{key} => {value}')

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)
