'''
Input: float from 0 to 360 inclusive
Output: string

Explicit:
    - represent the angle in degrees°, minutes', and seconds"
    - DEGREE = "\u00B0"
    - 60 minutes in a degree
    - 60 seconds in a minute

Implicit:
    - 

Questions:
    - how do i convert a decimal to angle format?

Data structures:
    - 

Algorithm:
    1. Calcualte degree format
        A. Degrees = whole number
        B: 60 * decimal --> whole number = minutes
        C: 60 * decimal --> whole number rounded = seconds
    2. Convert to string
    3. Return string

'''
from math import modf

DEGREES = '\u00B0'

def make_within_360(number):
    factor = abs(number // 360)    
    if number < 0:
        number += (factor * 360)
    elif number > 360:
        number -= (factor * 360)
    return number

def dms(number):
    number = make_within_360(number)
    
    dec, degrees = modf(number) 
    dec, minutes = modf(dec * 60)
    dec, seconds = modf(dec * 60)
    
    return f"{int(degrees)}{DEGREES}{int(minutes):02d}'{int(seconds):02d}\""

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

print(dms(-1))   # 359°00'00"
print(dms(400))  # 40°00'00"
print(dms(-40))  # 320°00'00"
print(dms(-420)) # 300°00'00"
