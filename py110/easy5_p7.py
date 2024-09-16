'''
input: positive integer
output: integer (sum of digits)

explicit rules:
- return sum of digits

implicit rules:
- 

questions:
- 

data structures:
- list

algorithm:
1. isolate each digit
2. sum all digits
3. return sum

'''
def sum_digits(num):
    sum = 0
    while num:
        num, remainder = divmod(num, 10)
        sum += remainder
    return sum

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True
