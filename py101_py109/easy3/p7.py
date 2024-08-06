def twice(n):
    str_n = str(n)
    length = len(str_n)
    if length % 2 == 0:
        mid = length // 2
        if str_n[:mid] == str_n[mid:]:
            return n
    return n * 2


print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True
