def get_grade(a, b, c):
    avg = (a + b + c) / 3
    if avg >= 90:
        return 'A'
    elif 80 <= avg <= 89:
        return 'B'
    elif 80 <= avg <= 89:
        return 'B'
    elif 70 <= avg <= 79:
        return 'C'
    elif 60 <= avg <= 69:
        return 'D'
    else: return 'F'

print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True
