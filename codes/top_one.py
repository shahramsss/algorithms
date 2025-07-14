"""
[1,1,1,1,1,3,3,3,3,3,2,2] = [1,3]
"""


def top_one(arr):
    values = {}
    result = []
    f_val = 0

    for i in arr:
        if i in values:
            values[i] += 1
        else:
            values[i] = 1
    f_val = max(values.values())

    for i in values.keys():
        if values[i] == f_val:
            result.append(i)
        continue

    return (result, f_val)


print(top_one([1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 2, 2]))
