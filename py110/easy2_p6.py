'''
Input: list of pos ints
Output: string with value of mult. avg. rounded to 3 dec

Explicit:
    - all ints are +
    - 

Implicit:
    - no empty lists

Questions:
    - 

Data structures:
    - 

Algorithm:
    1. Initialize avg to 1
    2. Iterate through list
        - multiple avg by element
    3. Divide avg by length
    4. return as string 

'''

def multiplicative_average(lst):
    mult_avg = 1
    for ele in lst:
        mult_avg *= ele
    
    mult_avg /= len(lst)

    return f'{mult_avg:.03f}'


# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")
