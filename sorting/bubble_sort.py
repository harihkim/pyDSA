# inplace
def bubble_sort(arr: list):
    size = len(arr)

    for i in range(size - 1):
        swaped = False
        for j in range(size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaped = True
        if not swaped:
            break
        else:
            swaped = False


if __name__ == "__main__":
    myArr = [4, 3, 2, 1]
    bubble_sort(myArr)
    print(myArr)
