# recursion
'''def triangle(n):
    # base case
    if n == 0:
        return 0
    
    # print spaces (original n - current n) and stars (current n)

    print((' ') + ('*' * n))
    triangle(n - 1)'''

def triangle2(n):
    spaces = n
    stars = 1
    while spaces >= 0:
        print((' ' * spaces) + ('*' * stars))
        spaces -= 1
        stars += 1

# triangle(5)


triangle2(5)
