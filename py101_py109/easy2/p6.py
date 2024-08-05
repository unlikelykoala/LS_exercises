def penultimate(string_):
    if not string_ or len(string_.split()) < 2:
        return 'Error: Please enter a multiword string'
    return string_.split()[-2]

def middle_word(string_):
    if not string_:
        return 'Error: Please enter a multiword string'
    
    words = string_.split()
    word_count = len(words)
    if word_count < 2:
        return 'Error: Please enter a multiword string'
    
    # odd
    elif word_count % 2 == 1:
        middle_index = int(word_count / 2)
        return words[middle_index]

    # even
    else:
        middle_index = int(word_count / 2)
        return f'{words[middle_index - 1]} and {words[middle_index]}'


print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")

print(middle_word("last dumb word") == "dumb")
print(middle_word("last word in here") == "word and in")
