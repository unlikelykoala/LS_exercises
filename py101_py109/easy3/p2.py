def crunch(str):
    str_len = len(str)
    if str_len < 2:
        return str
    new = ''
    for i in range(0, str_len):
        if i == 0 or str[i] != str[i-1]:
            new += str[i]
    
    return new


print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')
