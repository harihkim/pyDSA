# https://leetcode.com/problems/set-mismatch/description/


def cyclic_sort(nums: list[int]):
    i = 0
    size = len(nums)
    while i < size:
        correctIndex = nums[i] - 1
        if nums[i] != nums[correctIndex]:
            nums[i], nums[correctIndex] = nums[correctIndex], nums[i]
        else:
            i += 1


def find_misMatch(nums: list[int]):
    cyclic_sort(nums)
    for i in range(0, len(nums)):
        if nums[i] != i + 1:
            return [nums[i], i + 1]


if __name__ == "__main__":
    nums = [8, 7, 3, 5, 3, 6, 1, 4]
    print(find_misMatch(nums))
