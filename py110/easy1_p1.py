'''
Input: 6 numbers (string bc of input())
Output: String stating if the 6th number is in 1st 5

Explicit rules:
    - check if last number in first 5

Implicit rules:
    - input is returned as a string

DS: list

Algorithm:
    1. Ask user 6 times for a number
    2. Store 1st 5 numbers in a list
    3. Print statement of whether 6th number is among 1st 5.
'''

lst = []
lst.append(input('Enter the 1st number: '))
lst.append(input('Enter the 2nd number: '))
lst.append(input('Enter the 3rd number: '))
lst.append(input('Enter the 4th number: '))
lst.append(input('Enter the 5th number: '))

sixth = input('Enter the last number: ')

if sixth in lst:
    print(f'{sixth} is in {','.join(lst)}.')
else:
    print(f'{sixth} isn\'t in {','.join(lst)}.')
