'''
Input: string (first name last name)
Output: string (lastname, firstname)

Explicit:
    - return a new string consisting of 
        the last name, a comma, a space, and the first name
    - 

Implicit:
    - 

Questions:
    - 

Data structures:
    - 

Algorithm:
    1. split
    2. join with ', '
    3. return
'''

def swap_name(name):
    return f'{name.split()[-1]}, {' '.join(name.split()[0:-1])}'


print(swap_name('Karl Oskar Henriksson Ragvals')
                == "Ragvals, Karl Oskar Henriksson")  # True
