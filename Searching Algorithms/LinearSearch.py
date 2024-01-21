'''
fast for small and medium data sets, burt bad for large data sets.
does not needs to be sorted array
useful for datasets, that dont have rand access (like linked lists)

time complexity of it is O(n)
'''


def linearSort(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1