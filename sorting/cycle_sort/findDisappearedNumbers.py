# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/solutions/1583741/time-o-n-space-o-1/


def cycle_sort(nums: list[int]):  # for range [1 to n]
    i = 0
    while i < len(nums):
        correctIndex = nums[i] - 1
        if nums[i] != nums[correctIndex]:
            temp = nums[i]
            nums[i] = nums[correctIndex]
            nums[correctIndex] = temp
        else:
            i += 1
    return nums


def findMissing(nums: list[int]):
    cycle_sort(nums)
    missing = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            missing.append(i + 1)
    return missing


if __name__ == "__main__":
    arr = [4, 3, 2, 7, 8, 2, 3, 1]
    print(findMissing(arr))
