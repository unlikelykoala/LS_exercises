def oddities(lst):
    oddies = []
    for i in lst:
        if lst.index(i) % 2 == 0:
            oddies.append(i)
    
    return oddies

def oddities2(lst):
    oddies = []
    for i in range(0, len(lst), 2):
        oddies.append(lst[i])
    
    return oddies

def oddities3(lst):
    oddies = lst[::2]
    
    return oddies

print(oddities2([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities2([1, 2, 3, 4]) == [1, 3])        # True
print(oddities2(["abc", "def"]) == ['abc'])     # True
print(oddities2([123]) == [123])                # True
print(oddities2([]) == [])                      # True
