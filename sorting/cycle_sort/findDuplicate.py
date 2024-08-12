# https://leetcode.com/problems/find-the-duplicate-number/


def cyclic_sort(nums: list[int]):
    i = 0
    size = len(nums)
    while i < size:
        correctIndex = nums[i] - 1
        if nums[i] != nums[correctIndex]:
            nums[i], nums[correctIndex] = nums[correctIndex], nums[i]
        else:
            i += 1


def findDuplicate(nums: list[int]):
    cyclic_sort(nums)
    for index, value in enumerate(nums):
        if index != value - 1:
            return value


if __name__ == "__main__":
    nums = [3, 1, 3, 4, 2]
    print(findDuplicate(nums))
