def century(y):
    # calculate
    cen = 0
    if y % 100 != 0:
        cen = y // 100 + 1
    else: cen = y // 100

    # match case for number ending
    if 10 < cen and str(cen)[-2:] in ['11', '12', '13']:
        return f'{cen}th'
    ending = str(cen)[-1]
    print(cen)
    match ending:
        case '1':
            return f'{cen}st'
        case '2':
            return f'{cen}nd'
        case '3':
            return f'{cen}rd'
        case _:
            return f'{cen}th'


print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True
