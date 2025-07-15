"""
[121,,1,432,564,23,45,788]
"""


def radis_sort(array):
    position = 1
    max_number = max(array)

    while position < max_number:
        queue_list = [list() for _ in range(10)]

        for num in array:
            digit_number = num // position % 10
            queue_list[digit_number].append(num)

        print(queue_list)
        index = 0
        for numbers in queue_list:
            for num in numbers:
                array[index] = num
                index += 1
        position *= 10
        print(array)

    return array


print(radis_sort([121, 1, 432, 564, 23, 45, 788]))
