"""
[3,4,5,6,8,9,11,13,15,17,20,23,24,25,37]
sorted data
indx
[(low) , .... , (mid-1) , (mid) , (mid+1) , .... , (high)]
"""


def binary_search(array, element):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        val = array[mid]
        if val == element:
            return mid

        if val < element:
            low = mid + 1
        else:
            high = mid - 1
    return None


print(binary_search([3,4,5,6,8,9,11,13,15,17,20,23,24,25,37] , 11))