# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/


def cycle_sort(nums: list[int]):
    i = 0
    while i < len(nums):
        correctIndex: int = nums[i] - 1
        if nums[i] != nums[correctIndex]:
            nums[correctIndex], nums[i] = nums[i], nums[correctIndex]
        else:
            i += 1
    return nums


def findAllDuplicate(nums: list[int]):
    cycle_sort(nums)
    duplicates = set()
    for index, value in enumerate(nums):
        if index != value - 1:
            duplicates.add(value)
    return list(duplicates)


if __name__ == "__main__":
    arr = [4, 3, 2, 7, 8, 2, 3, 1]
    cycle_sort(arr)
    print(findAllDuplicate(arr))
