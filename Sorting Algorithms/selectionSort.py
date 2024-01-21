def selectionSort(arr):
    for i in range(len(arr) - 1):
        min = i
        for j in range(i, len(arr)):
            if(arr[min] > arr[j]):
                min = j
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp
        
'''
worst case O(n^2)

'''