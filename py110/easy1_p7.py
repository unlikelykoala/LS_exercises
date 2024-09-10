'''
Input: string of words sep by spaces
Output: string with first and last letters of all words swapped

Explicit:
    - swap first and last letters of all words
    - no leading/trailing/repeated spaces
    - words and single spaces only

Implicit:
    - maintain case

Questions:
    - can input be empty string?
    - what about puncuation?

Data structures:
    - list
    - string

Algorithm:
    1. Convert input string to list of words
    2. Create empty string for swapped output
    2. Iterate through list
        A: Create empty string for new word
        B: Concatenate last letter + middle + first letter
        C: Concatenate space + new word to swapped string
    3. Return swapped string

'''
def letter_swap(word):
    swap_word = word[-1] + word[1:-1] + word[0]
    return swap_word

def swap(words):
    words_lst = words.split()

    swap_lst = []

    for word in words_lst:
        swap_word = word
        if len(word) > 1:
            swap_word = letter_swap(word)
        
        swap_lst.append(swap_word)
    
    return ' '.join(swap_lst)


print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
