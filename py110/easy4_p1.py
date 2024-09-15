'''
input: list of ints between 0 and 19 inclusive
output: list of the same ints sorted based on the english word for each number

explicit rules:
- return new list
- sort based on english word for each number 
- from a to z

implicit rules:
- 

questions:
- 

data structures:
- list

algorithm:
1. Make a dictionary with int as key and word as value
2. function to sort based on the words


'''

NUMS_DICT = {
    0: 'zero',  
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}

# WORDS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
#          'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
#            'sixteen', 'seventeen', 'eighteen', 'nineteen',]

def alphabetic_number_sort(lst):
    tups_list = sorted([(NUMS_DICT[num], num) for num in lst])

    return [num for word, num in tups_list]


input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)
# Prints True
