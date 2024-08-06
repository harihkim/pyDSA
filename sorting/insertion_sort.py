def insertion_sort(arr: list[int | float]):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and current < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr


def insertion_sort2(arr: list[int | float]):
    for i in range(1, len(arr)):
        current = arr[i]
        for j in range(i - 1, -1, -1):
            if current < arr[j]:
                arr[j + 1] = arr[j]
            else:
                break
        arr[j] = current
    return arr


if __name__ == "__main__":
    print(insertion_sort([4, 5, 3, 7, 6, 2]))
