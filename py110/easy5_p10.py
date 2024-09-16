'''
input: seq of ints (list, range, or tuple)
output: dict with keys-values inverted

explicit rules:
- remove elements where consecutive numbers are the same, keep only the first

implicit rules:
- maybe always a list

questions:
- do i mutate or return a new seq?
- will it always be a list?

data structures:
- list

algorithm:
1. create empty list
2. iterate through list
    - if the previous number is not the same, append the current number
3. return new list

'''
# def unique_sequence(nums):
#     filtered = []
#     for idx in range(len(nums)):
#         if idx == 0 or nums[idx] != nums[idx-1]:
#             filtered.append(nums[idx])
#     return filtered

def unique_sequence(nums):
    return [nums[idx] for idx in range(len(nums))
            if idx == 0 or nums[idx] != nums[idx-1]]

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True
