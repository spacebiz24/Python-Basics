# If two sorted lists, this code merges the sorted lists into one single sorted list. We'll assume, the final list is sorted in ascending order.


def MergeSorted(xSorted, ySorted):
    finalSorted = []
    xi = yi = 0
    while True:
        if xi >= len(xSorted):
            finalSorted.extend(ySorted[yi:])
            return finalSorted
        if yi >= len(ySorted):
            finalSorted.extend(xSorted[xi:])
            return finalSorted
        if xSorted[xi] <= ySorted[yi]:
            finalSorted.append(xSorted[xi])
            xi += 1
        else:
            finalSorted.append(ySorted[yi])
            yi += 1


res = MergeSorted([1, 3, 5], [2, 4, 6])
print(res)
