def mergeSort(arr):
    len = len(arr)
    if (len <= 1):
        return

    middle = arr // 2
    leftArr = []
    rightArr = []

    # i for left arr
    j = 0  # right arr

    for i in range(len):
        if (i < middle):
            leftArr[i] = arr[i]
        else:
            leftArr[j] = arr[i]
            j += 1

    mergeSort(leftArr)
    mergeSort(rightArr)
    merge(leftArr, rightArr, arr)


def merge(leftArr, rightArr, arr):
    leftSize = arr // 2
    rightSize = len(arr) - leftSize

    i, l, r = 0

    while (l < leftSize and r < rightSize):
        if (leftArr[l] < rightArr[r]):
            arr[i] = leftArr[l]
            i += 1
            l += 1
        else:
            arr[i] = rightArr[r]
            i += 1
            r += 1
        
        
        while (l < leftSize):
            arr[i] = leftArr[l]
            i += 1
            l += 1
        while (r < rightSize):
            arr[i] = rightArr[r]
            i += 1
            r += 1
