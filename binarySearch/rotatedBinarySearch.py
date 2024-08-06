# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
# search-in-rotated-sorted-array

# find the index of pivot (peak) element of array
# then we get two sorted array - search in then using binary search


def findPivot(arr: list):
    start = 0
    end = len(arr) - 1

    while (start <= end):
        mid = (start + end) //2
        if (mid < end and arr[mid] > arr[mid+1]):
            return mid
        elif( mid > start and arr[mid] < arr[mid-1]):
            return mid-1
        elif(arr[start] >= arr[mid]):
            end = mid - 1
        else:
            start = mid + 1
    return -1

# def binarySearch(arr: list, toFind: int): # don't use
#     s = 0
#     e = len(arr) - 1
#     while(s <= e):
#         mid = (s + e)//2
#         if(arr[mid] == toFind):
#             return mid
#         elif(toFind > arr[mid]):
#             s = mid + 1
#         else:
#             e = mid - 1
#     return -1

def binarySearch(arr: list, toFind: int, s, e):
        while(s <= e):
            mid = (s + e)//2
            if(arr[mid] == toFind):
                return mid
            elif(toFind > arr[mid]):
                s = mid + 1
            else:
                e = mid - 1
        return -1

def search(arr: list, target: int):
    pivotIndex = findPivot(arr)
    print(pivotIndex)
    if(pivotIndex == -1): #if we can't find pivot, it is not rotated so plain binary search
        return binarySearch(arr, target, 0, len(arr)-1)
    else:
        index = binarySearch(arr, target, 0, pivotIndex) 
        if(index != -1):
            return index
        else:
            return binarySearch(arr, target, pivotIndex+1, len(arr)-1)

myarr = [2,9,2,2,2]
index = search(myarr, 2)
print(index)
