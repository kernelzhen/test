arr = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45,5000]
"""
找到最大的2个数
"""
max_num = 0
sec_num = 0
for i in arr:
    if i > sec_num and i < max_num:
        sec_num = i
    elif i > max_num:
        sec_num == max_num
        max_num = i

print(max_num)
print(sec_num)