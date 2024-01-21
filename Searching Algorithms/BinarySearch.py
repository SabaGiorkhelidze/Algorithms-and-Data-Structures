'''
time complexity of this algorithm is O(log n) which makes it ideal for big datasets
'''

def binarySearch(arr, target):
    low = 0
    high = len(arr)-1
    
    
    while(low <= high):
        middle = low + (high - low) // 2
        value = arr[middle]
        
        if(value < target):
            low = middle + 1
        elif(value > target):
            high = middle - 1
        else:
            return middle
    
    return -1