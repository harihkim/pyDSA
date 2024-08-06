# https://www.geeksforgeeks.org/find-rotation-count-rotated-sorted-array/
# Find the Rotation Count in Rotated Sorted array

# find peak index + 1 == no. of times rotated
def rotationCount(arr: list):
    start = 0
    end = len(arr) - 1

    while (start <= end):
        mid = (start + end) // 2

        if(mid < end  and arr[mid] > arr[mid+1]):
            return mid + 1
        elif(arr[mid] < arr[mid - 1]):
            return mid
        else:
            if(arr[mid] <= arr[start]):
                end = mid - 1
            else:
                start = mid + 1
    return 0

myArr = [11]
print(rotationCount(myArr))