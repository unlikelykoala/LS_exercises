def stringy(length):
    bin_string = ''
    for i in range(1, length +1):
        if i % 2 == 1: bin_string += '1'
        else: bin_string += '0'
    return bin_string

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")   
