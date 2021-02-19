import time


array1 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
array2 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
array3 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
array4 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def selectSort(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array


def insertSort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            while array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
    return array


def quickSort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
        else:  # 엇갈린 경우
            array[pivot], array[right] = array[right], array[pivot]
    quickSort(array, start, right - 1)
    quickSort(array, right + 1, end)
    return array


def quickSort2(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]
    return quickSort2(left) + [pivot] + quickSort2(right)


print(selectSort(array1))
print(insertSort(array2))
print(quickSort(array3, 0, len(array3) - 1))
print(quickSort2(array4))
