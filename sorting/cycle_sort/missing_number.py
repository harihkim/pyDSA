# https://leetcode.com/problems/missing-number/description/


def cycle_sort(arr: list[int]):
    i: int = 0
    size = len(arr)
    while i < size:
        if arr[i] == size:
            i += 1
        elif arr[i] != i:
            temp = arr[i]
            arr[i] = arr[temp]
            arr[temp] = temp
        else:
            i += 1


def missing_number(arr: list[int]):
    cycle_sort(arr)
    for i, v in enumerate(arr):
        if i != v:
            return i
    # case 2:
    return len(arr)


def missing_number2(arr: list[int]):
    size = len(arr)
    total = (size * (size + 1)) // 2
    missing = total - sum(arr)
    return missing


def missing_number3(arr: list[int]):
    size = len(arr)
    for i in range(0, size + 1):
        if i not in arr:
            return i


if __name__ == "__main__":
    arr = [3, 4, 2, 0]
    print(missing_number(arr))
