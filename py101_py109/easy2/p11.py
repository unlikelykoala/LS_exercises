def center_of(string_):
    if not string_:
        return 'Empty string.'
    str_len = len(string_)
    middle_index = str_len // 2
    if str_len == 1:
        return string_
    elif str_len % 2 == 1:
        return string_[middle_index]
    else:
        return string_[middle_index - 1 : middle_index + 1]


print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True
