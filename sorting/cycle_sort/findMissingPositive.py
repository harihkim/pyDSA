# https://leetcode.com/problems/first-missing-positive/


def cycleSort(nums: list[int]):
    """Modified cycle sort"""
    i = 0
    size = len(nums)
    while i < size:
        correctIndex = nums[i] - 1
        if nums[i] > 0 and nums[i] <= size and nums[i] != nums[correctIndex]:
            nums[i], nums[correctIndex] = nums[correctIndex], nums[i]
        else:
            i += 1


def firstMissingPositive(nums: list[int]):
    cycleSort(nums)
    for index in range(0, len(nums)):
        if nums[index] != index + 1:
            return index + 1
    return len(nums) + 1
