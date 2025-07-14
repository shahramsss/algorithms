"""
[3,4,5,6,8,9,11,13,15,17,20,23,24,25,37]
sorted data
indx
"""

import math


def jump_search(array, target):
    arr_size = len(array) - 1
    block_size = int(math.sqrt(arr_size))
    prev = 0
    step = block_size

    while array[min(step, arr_size)-1] < target:
        prev = step
        step += block_size
        if prev >= arr_size:
            return -1

    while array[prev] < target:
        prev += 1
        if prev == min(step, arr_size):
            return -1

    if array[prev] == target:
        return prev
    return -1


print(jump_search([3, 4, 5, 6, 8, 9, 11, 13, 15, 17, 20, 23, 24, 25, 37], 5))
