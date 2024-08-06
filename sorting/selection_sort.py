def selectionSort1(arr: list[int | float]):
    size = len(arr)
    for i in range(size - 1):
        maxValue, index = arr[0], 0
        for j in range(size - i):
            if arr[j] > maxValue:
                maxValue, index = arr[j], j
        arr[size - 1 - i], arr[index] = arr[index], arr[size - i - 1]
    return arr


def selectionSort0(arr: list[int | float]):
    size = len(arr)
    for i in range(size - 1):
        maxIndex = 0
        for j in range(size - i):
            if arr[j] > arr[maxIndex]:
                maxIndex = j
        arr[size - 1 - i], arr[maxIndex] = arr[maxIndex], arr[size - i - 1]
    return arr


print(selectionSort0([2, 1]))
