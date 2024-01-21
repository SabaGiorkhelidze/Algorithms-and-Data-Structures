def bublesort(arr: list[int]) -> list[int]:
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if (arr[j] > arr[j+1]):
                temp: int = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr


def binary_search(arr: list[int], target: int) -> (int, int or str, int):
    low: int = 0
    high: int = len(arr) - 1
    iteration_counter: int = 0
    while (low <= high):
        middle: int = low + (high - low) // 2
        value: int = arr[middle]

        if (value < target):
            low = middle + 1
        elif (value > target):
            high = middle - 1
        else:
            return middle, iteration_counter

        iteration_counter += 1

    return 'not found', iteration_counter


def task_one(arr: list[int], k: int) -> (int, int) or (str, int):
    length: int = len(arr)
    sorted_arr: list[int] = bublesort(arr=arr)
    return binary_search(sorted_arr, k)


# _______________________________________________________________________________________________________________________________________________#

def find_biggest_negative(arr):
    arr = [num for num in arr if num < 0]
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max


# print(find_biggest_negative([6, -7, -9, -100, -3, 11, 23]))
'''
sort --> * all except 0 and 1 --> if negative / on the biggest 
'''


def task_two(arr):
    new_arr = []
    for i in range(len(arr)):
        if arr[i] != 0 and arr[i] != 1:
            new_arr.append(arr[i])
    res = 1
    for num in new_arr:
        res *= num
    if res < 0:
        negative = find_biggest_negative(new_arr)
        res /= negative
        new_arr.remove(negative)
    return new_arr, res

print(task_two([0, 3, 6, 7, 8, 1, 1, 0, -9,-2,-29, -25,-1, -3, -77, -11]))
