def multiply(x, y):
    return x * y

def square(num):
    return multiply(num, num)

def power_n(num, n):
    if n == 0:
        return 1
    else:
        return multiply(num, power_n(num, n - 1))

print(square(5) == 25)   # True
print(square(-8) == 64)  # True

print(f'Power function evaluates as {power_n(2, 4) == 16}')   # True
