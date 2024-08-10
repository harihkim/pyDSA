# https://leetcode.com/problems/find-the-duplicate-number/


def find_duplicate(nums: list[int]):
    exsisting = set()
    for num in nums:
        if num in exsisting:
            return num
        else:
            exsisting.add(num)
    return None


if __name__ == "__main__":
    arr = [1, 4, 3, 4, 2]
    print(find_duplicate(arr))
