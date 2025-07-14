"""
[2,2,4,4,4,6,6,6,7,7,7,7,7,] -> 6 =>5
sorted
"""

def first_occurrence(array, target):
    low, high = 0, len(array) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            result = mid
            high = mid - 1  # بگرد دنبال مورد قبلی
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result

# تست
print(first_occurrence([2, 2, 4, 4, 4, 6, 6, 6, 7, 7, 7, 7, 7, 8], 2))  # خروجی: 0
print(first_occurrence([2, 2, 4, 4, 4, 6, 6, 6, 7, 7, 7, 7, 7, 8], 6))  # خروجی: 5
print(first_occurrence([2, 2, 4, 4, 4, 6, 6, 6, 7, 7, 7, 7, 7, 8], 9))  # خروجی: -1
