'''
Input: string of time in 24 hr format (HH:MM)
Output before: time before midnight in mins
Output after: time after midnight in mins

Explicit:
    - return format is 'hh:mm'
    - cannot use datetime module
    - ignore daylight savings and similar complications

Implicit:
    - 00:00 is possible (midnight)
    - input can be so high/low that it loops several days

Questions:
    - 

Data structures:
    - 

Algorithm:
    1. Extract hrs and mins from string
    2. Convert hrs and mins to int
    3. Calculate total mins
    4. Normalize mins to be within 1 day
    5. After:
        - return normalized mins
    5. Before:
        - return mins per day minus normalized mins


'''
MINS_PER_HR = 60
HRS_PER_DAY = 24
MINS_PER_DAY = MINS_PER_HR * HRS_PER_DAY

# def timestring_to_int(time_str):
#     hr = int(time_str[:2])
#     min = int(time_str[3:])
#     return hr, min

# def get_delta_min(hr, min):
#     return (hr * MINS_PER_HR) + min


# def after_midnight(time_str):
#     hr, min = timestring_to_int(time_str)

#     delta_min =  get_delta_min(hr, min)

#     return delta_min % MINS_PER_DAY

# def before_midnight(time_str):
#     hr, min = timestring_to_int(time_str)
    
#     delta_min = get_delta_min(hr, min)
    
#     day_minus_delta = MINS_PER_DAY - delta_min

#     return day_minus_delta % MINS_PER_DAY
import datetime as dt

TIME_FORMAT = '%H:%M'

def format_for_strptime(time_str):
    if time_str == '24:00':
        return '00:00'
    return time_str

def after_midnight(time_str):
    time_str = format_for_strptime(time_str)
    time = dt.datetime.strptime(time_str, TIME_FORMAT)
    hours = time.hour
    minutes = time.minute
    delta_min = (hours * MINS_PER_HR) + minutes
    return delta_min

def before_midnight(time_str):
    min_time = after_midnight(time_str)
    delta_min = (MINS_PER_DAY - min_time) % MINS_PER_DAY
    return delta_min


print(after_midnight("00:00") == 0)     # True

# print(before_midnight("00:00"))
print(before_midnight("00:00") == 0)    # True

# print('after 12:34:', after_midnight("12:34"))
print(after_midnight("12:34") == 754)   # True

# print('before 12:34 -- ', before_midnight("12:34"))
print(before_midnight("12:34") == 686)  # True

print(after_midnight("24:00") == 0)     # True

# print('before 24:00', before_midnight("24:00"))
print(before_midnight("24:00") == 0)    # True
