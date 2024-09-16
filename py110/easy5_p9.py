'''
input: string
output: strign with staggered capitalization

explicit rules:
- start capital from 1st letter
- then every other letter will be capital (odds)
- non-alpha chars count as chars

implicit rules:
- empty string returns empty string
- change upper even chars to lower

questions:
- 

data structures:
- str

algorithm:
1. create new string
2. create odd_even
2. iterate through input string
    - if alpha, then add upper or lower, increment count
    - if non-alpha, add without incrementing count
    - note: 0 is the 1st position, so even idx represent odd positions

'''
def staggered_case(my_str):
    new_str = ''
    up_or_low = 1
    
    for char in my_str:
        if char.isalpha():
            if up_or_low:
                new_str += char.upper()
                up_or_low -= 1
            else:
                new_str += char.lower()
                up_or_low += 1
        else:
            new_str += char
    
    return new_str

string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True
