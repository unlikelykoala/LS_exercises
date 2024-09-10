'''
Input: string with 0 or more space-separate words
Output: dict with length of word as key and num of words as value

Explicit:
    - will need to turn string into list
    - exclude non-letters from word lengths

Implicit:

Questions:
    - does that mean that it could contain 0 words 
      or that it could 0 or more spaces?
    - 

Data structures:
    - list
    - dictionary

Algorithm:
    1. Convert input string to list of words
    2. Iterate through list
        A: for each word, remove non-letters
            1. Create empty string 
            2. Iterate through characters
            3. If alpha, append char to new string
        B: get the length
        C: If not in dict: Initialize length to dict as key with value 0
        D: incremenet value by 1
    3. Return dict

'''

def word_sizes(words):
    words_lst = words.split()

    length_count = {}

    for word in words_lst:
        clean_word = ''
        for char in word:
            if char.isalpha():
                clean_word += char

        length = len(clean_word)

        if length not in length_count:
            length_count[length] = 0
        length_count[length] += 1
    
    return length_count

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})
