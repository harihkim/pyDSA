def cycleSort(nums: list[int]):
    i = 0
    size = len(nums)
    while i < size:
        correctIndex = nums[i] - 1
        if nums[i] != nums[correctIndex]:
            nums[i], nums[correctIndex] = nums[correctIndex], nums[i]
        else:
            i += 1


def cycleSort2(arr: list[int]):
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


if __name__ == "__main__":
    arr = [4, 3, 2, 1]
    cycleSort(arr)
    print(arr)
