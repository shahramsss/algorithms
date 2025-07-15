"""'
[False, 1, 3, 4, 5, 6, 0, 4, 6, 8, 9, 0, 8, 9, 0]
"""


def move_zeroes(array):
    result = []
    zeroes = 0

    for i in array:
        if i == 0 and type(i) != bool:
            zeroes += 1
        else:
            result.append(i)
    result.extend([0]*zeroes)    
    return result


print(move_zeroes([False, 1, 3, 4, 5, 6, 0, 4, 6, 8, 9, 0, 8, 9, 0]))
