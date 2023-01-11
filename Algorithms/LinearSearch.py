# Linear Search travels from one end of the array to the other end to search for the element and returns the index.


def LinearSearch(element, array):
    index = -1
    for i in range(len(array)):
        if array[i] == element:
            index = i
    if index == -1:
        print("{} not found!".format(element))
    else:
        print("{} found at index {}!".format(element, index))


LinearSearch(1, [3, 4, 5, 6, 3, 5, 1])
