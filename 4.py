arr = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
new_arr = []
for i in arr:
    if i not in new_arr:
        new_arr.append(i)



print(new_arr)