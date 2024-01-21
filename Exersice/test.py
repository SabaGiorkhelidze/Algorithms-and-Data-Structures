def bubleSort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                
                

def selectionSort(arr):
    for i in range(len(arr) - 1):
        min = i
        for j in range(i, len(arr)):
            if arr[min] > arr[j]:
                min = j
            
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp 
        


def inserTionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while(j >= 0 and arr[j] > temp):
            arr[j]