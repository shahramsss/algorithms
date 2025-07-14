"""
[2,2,4,4,4,6,6,6,7,7,7,7,7,8] -> 6 =>7
sorted
"""


def last_occurrence(array, target):
    low, high = 0, len(array) - 1

    while low <= high:
        mid = (high + low) // 2

        if (array[mid]==target and mid == (len(array)-1) or array[mid]==target and array[mid+1]>target):
            return mid
        elif array[mid]<= target:
            low = mid +1
        else:
            high = mid -1 
        


def last_occurrence2(array, target):
    low, high = 0, len(array) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] == target:
            result = mid           # ذخیره کن
            low = mid + 1          # برو سمت راست ببین مورد آخری هست یا نه
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result

print(last_occurrence([2,2,4,4,4,6,6,6,7,7,7,7,7,8],4 ))
print(last_occurrence2([2,2,4,4,4,6,6,6,7,7,7,7,7,8],4 ))