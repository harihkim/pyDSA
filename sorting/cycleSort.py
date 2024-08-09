def cycleSort(arr: list[int]):
    i = 0
    for i in range(len(arr)):
        while arr[i] != i + 1:
            temp = arr[i]
            arr[i] = arr[temp - 1]
            arr[temp - 1] = temp


if __name__ == "__main__":
    arr = [4, 3, 2, 1]
    cycleSort(arr)
    print(arr)
