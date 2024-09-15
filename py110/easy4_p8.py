'''
input: string
output: list of all substrings that are palindromes

explicit rules:
- all substrings
- order based on order of appearance
- must be palindrome

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
def subsubstrings(sub):
    return [sub[:idx+1] for idx in range(len(sub))]
def substrings(str_input):
    subs = []
    for idx in range(len(str_input)):
        subs += subsubstrings(str_input[idx:])
    return subs
def palindromes(str_input):
    return [ele for ele in substrings(str_input)
            if ele == ele[::-1] and len(ele) > 1]
    


print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True
