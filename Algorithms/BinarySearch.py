# Binary Search works only with sorted lists and in each consecutive step, divides its searchable area by half until it gets a hit on the element.


def BinarySearch(element, array):
    high = len(array) - 1
    low = 0
    index = -1
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == element:
            index = mid
            break
        elif array[mid] < element:
            low = mid + 1
        elif array[mid] > element:
            high = mid - 1
    if index == -1:
        print("{} not found!".format(element))
    else:
        print("{} found at index {}".format(element, index))


BinarySearch(3, [1, 2, 3, 4, 5, 6, 7, 8])
