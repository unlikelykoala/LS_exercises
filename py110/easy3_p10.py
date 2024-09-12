'''
Input: string
Output: bool (True if balanced parentheses, False if not)

Explicit:
    - parentheses must occur in matching '(' and ')' pairs
    - pair must start with ( not )

Implicit:
    - 

Questions:
    - 

Data structures:
    - 

Algorithm:
    1. Count occurrences of ( and )
        - if not equal, return False
        - if both = 0, return False
    2. search for (
        - maybe use index or find or count
        - mayeb first check if the count is equal, then continue to check they match with index
    2. Find matching )
    3. Return False if no matching or starts with )
    idea: make 2 lists of indices for ( and )? then compare?

'''

def is_balanced(text):
    left_count = 0
    right_count = 0
    
    for char in text:
        if char == '(': left_count += 1
        elif char == ')': right_count += 1
        if right_count > left_count: return False
    
    return left_count == right_count

print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True
