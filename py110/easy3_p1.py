'''
Input: pos or neg int (minutes before or afte rmidnight)
Output: string (time, 24hr format 'hh:mm')

Explicit:
    - all ints are +
    - return format is 'hh:mm'
    - cannot use datetime module
    - ignore daylight savings and similar complications

Implicit:
    - 0 is possible (midnight)
    - input can be so high/low that it loops several days

Questions:
    - 

Data structures:
    - 

Algorithm:
    1. Get hours using int division (minutes // 60) and modulo (ans %n 24)
    2. Get remaining minutes using modulo (minutes % 60) 
    3. If pos/neg, add to 00:00 or subtract from 24:60
    3. Convert to string
        - 00 format
'''
MIN_PER_HR = 60
HRS_PER_DAY = 24

# def format_time(minutes, hrs_r, mins_r):
#     if minutes >= 0:
#         return f'{hrs_r:02d}:{mins_r:02d}'
    
#     return f'{23 - hrs_r:02d}:{MIN_PER_HR - mins_r:02d}'

# def time_of_day(minutes):    
#     minutes_abs = abs(minutes)
    
#     hours_remaining = (minutes_abs // MIN_PER_HR) % HRS_PER_DAY
#     minutes_remaining = minutes_abs % MIN_PER_HR
    
#     return format_time(minutes, hours_remaining, minutes_remaining)

import datetime as dt

def time_of_day(mins):
    time = dt.datetime(2024, 9, 15, 0, 0, 0)
    time_change = dt.timedelta(minutes=mins)
    new_time = time + time_change
    return new_time.strftime('%A %H:%M')

print(time_of_day(-4231))
# print(time_of_day(0) == "00:00")        # True
# print(time_of_day(-3) == "23:57")       # True
# print(time_of_day(35) == "00:35")       # True
# # print(time_of_day(-1437))
# print(time_of_day(-1437) == "00:03")    # True
# print(time_of_day(3000) == "02:00")     # True
# print(time_of_day(800) == "13:20")      # True
# # print(time_of_day(-4231))
# print(time_of_day(-4231) == "01:29")    # True
