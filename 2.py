"""
冒泡排序

"""

lst = [3, 5, 55, 1, 32, 4]

# for i in lst:
#     for j in range(len(lst)-1):
#         if lst[j] > lst[j+1]:
#             lst[j], lst[j+1] = lst[j+1],lst[j]


for j in range(len(lst)-1):
    if lst[j] > lst[j+1]:
        lst[j], lst[j+1] = lst[j+1], lst[j]
    if lst[j] > lst[j + 1]:
        lst[j], lst[j + 1] = lst[j + 1], lst[j]
print(lst)
print(lst)