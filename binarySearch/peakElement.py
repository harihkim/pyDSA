# https://leetcode.com/problems/peak-index-in-a-mountain-array/

def peakElementIndex(arr: list):
    s = 0
    e = len(arr) - 1
    while(s < e):
        mid = (s + e)//2
        if(arr[mid + 1] > arr[mid]):
            s = mid + 1
        else:
            e = mid
    return e

