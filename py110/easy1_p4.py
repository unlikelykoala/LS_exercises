'''
Input: list of numbers (argument)
Output: list of numbers

Explicit rules:
    - return a list of the running total up to that point
        - e.g., the 2nd element will be the sum of 
        the first two elements of original list
    

Implicit rules:
    - 

Questions:
    - 

Data Structures:
    - list

Algorithm:
    1. CREATE new empty list
    2. Iterate through original list
        A. Sum the values in each iteration
        B. Set sum to next value in new list
    3. Return list
'''
def running_total(nums):
    new = []
    
    for idx in range(len(nums)):
        run_total = sum(nums[:idx+1])
        new.append(run_total)

    return new


print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True
