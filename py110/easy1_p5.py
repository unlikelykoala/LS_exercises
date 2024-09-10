'''
Input: string with 0 or more space-separate words
Output: dict with length of word as key and num of words as value

Explicit:
    - will need to turn string into list
    -

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
        A: for each word, get the length
        B: If not in dict: Initialize length to dict as key with value 1
        C: If in, incremenet value by 1
    3. Return dict

'''

def word_sizes(words):
    words_lst = words.split()

    length_count = {}

    for word in words_lst:
        length = len(word)
        if length not in length_count:
            length_count[length] = 1
        else:
            length_count[length] += 1
    
    return length_count

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})
