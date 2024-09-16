'''
input: string
output: list of every word from the string, a space, and the length of the string
['cow 3', ....]

explicit rules:
- return new list
- words separated by single space
- if empty string or no argument, return empty list

implicit rules:
- punctuation is included as a character in the words

questions:
- do i mutate or return a new dict?

data structures:
- dict

algorithm:
1. get list of words
2. get length of each word
3. add space and length to each word in list
4. return list

'''
def add_length(word):
    length = len(word)
    word += f' {length}'
    return word

def word_lengths(my_string=''):
    lst = my_string.split(' ')
    return [add_length(word) for word in lst
            if word]


# All of these examples should print True
words = 'cow sheep chicken'
expected_result = ['cow 3', 'sheep 5', 'chicken 7']
print(word_lengths(words) == expected_result)        # True

words = 'baseball hot dogs and apple pie'
expected_result = ['baseball 8', 'hot 3', 'dogs 4',
                   'and 3', 'apple 5', 'pie 3']
print(word_lengths(words) == expected_result)        # True

words = "It ain't easy, is it?"
expected_result = ['It 2', "ain't 5", 'easy, 5',
                   'is 2', 'it? 3']
print(word_lengths(words) == expected_result)        # True

big_word = 'Supercalifragilisticexpialidocious'
print(word_lengths(big_word) == [f'{big_word} 34'])  # True

print(word_lengths('') == [])                        # True
print(word_lengths() == [])                          # True
