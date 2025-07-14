"""
[10,3,4,6,7,9,2,8,12,14,15,11,17]
"""


def linear_search(arr, element):
    index = []
    for i, value in enumerate(arr):
        if value == element:
            index.append(i)
    return index

print("index:", linear_search([10, 3, 4, 6, 3, 7, 9, 2, 8, 12, 14, 15, 11, 17], 3))
