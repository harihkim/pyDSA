# https://leetcode.com/problems/two-sum/


def twoSum(nums: list[int], target: int):
    seen: dict[int, int] = {}
    for index, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], index]
        else:
            seen[num] = index


if __name__ == "__main__":
    arr = [2, 7, 11, 15]
    print(twoSum(arr, 9))
