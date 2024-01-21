def insertionSort(arr):
    for i in range(1, len(arr)):

        temp = arr[i]
        j = i - 1

        while (j >= 0 and arr[j] > temp):
            arr[j+1] = arr[j]
            j -= 1
            print(arr)
        arr[j+1] = temp
        
    return arr


print(insertionSort([2, 6, 8, 9, 1, 3, 7, 4, 5]))
