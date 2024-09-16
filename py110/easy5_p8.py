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
- do i mutate or return a new dict?

data structures:
- str

algorithm:
1. create new string
2. iterate through input string
3. capitalize and add even chars, add lower odd chars
    - note: 0 is the 1st position, so even idx represent odd positions

'''
# def staggered_case(my_str):
#     new_str = ''
#     for idx in range(len(my_str)):
#         if idx % 2 == 1:
#             new_str += my_str[idx].lower()
#         else:
#             new_str += my_str[idx].upper()
#     return new_str

def staggered_case(my_str):
    return ''.join([my_str[idx].upper() if idx % 2 == 0
                    else my_str[idx].lower()
                    for idx in range(len(my_str))])

string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True
