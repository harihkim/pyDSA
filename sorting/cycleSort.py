def cycleSort(arr: list[int]):
    i = 0
    while i < len(arr):
        if arr[i] != i + 1:
            temp = arr[i]
            arr[i] = arr[temp - 1]
            arr[temp - 1] = temp
        else:
            i += 1


def cycleSort1(arr: list[int]):
    i = 0
    for i in range(len(arr)):
        while arr[i] != i + 1:
            temp = arr[i]
            arr[i] = arr[temp - 1]
            arr[temp - 1] = temp


def cycleSort2(arr: list[int]):
    i = 0
    while i < len(arr):
        correctIndex = arr[i] - 1
        if arr[i] != arr[correctIndex]:
            temp = arr[correctIndex]
            arr[correctIndex] = arr[i]
            arr[i] = temp
        else:
            i += 1


if __name__ == "__main__":
    arr = [4, 3, 2, 1]
    cycleSort(arr)
    print(arr)
