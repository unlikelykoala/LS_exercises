'''
input: string
output: list of all substrings

explicit rules:
- all substrings
- order based on starting point

implicit rules:
- 

questions:
- 

data structures:
- list

algorithm:
1. loop through substring to get starting point
    A: loop with all strings after starting point to get all subs after that
    B: Add each substring to list
2. return list

'''
def substrings(str_input):
    return [str_input[idx1:idx2+1] for idx1 in range(len(str_input))
            for idx2 in range(idx1, len(str_input))]

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde'))# == expected_result)  # True
