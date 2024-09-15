'''
input: string
output: list of all substrings in input starting with first letter

explicit rules:
- must contain all substrings starting with the first letter
- shortest to longest

implicit rules:
- whole string is the final substring

questions:
- 

data structures:
- list

algorithm:
1. create empty list
2. iterate through the string
    - each iteration, add one char to string and append it to empty list
    - do this until the whole string is included
3. return list

'''
# def leading_substrings(str_input):
#     subs = []
#     word = ''

#     for idx in range(len(str_input)):
#         word += str_input[idx]
#         subs.append(word)
#         idx += 1

#     return subs
def leading_substrings(str_input):
    subs = [str_input[:idx+1] for idx in range(len(str_input))]

    return subs


# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])
