

def binarySearch(arr: list, toFind: int):
    s = 0
    e = len(arr) - 1

    while(s <= e):
        mid = (s + e)//2
        if(arr[mid] == toFind):
            return mid
        elif(toFind > arr[mid]):
            s = mid + 1
        else:
            e = mid - 1
    return -1

def orderAgnosticBinarySearch(arr: list, toFind: int) -> int:

    # based on whether the sorted array is ascending or descending order

    s = 0
    e = len(arr) - 1
    size = len(arr)

    while(s <= e):
        mid = (s + e)//2
        if(arr[mid] == toFind):
            return mid
        
        elif(arr[0] < arr[size-1]): # for ascending order
            if(toFind > arr[mid]):
                s = mid + 1
            else:
                e = mid - 1
        
        else:                       # descending order
            if(toFind > arr[mid]): 
                e = mid - 1
            else:
                s = mid + 1
    return -1

# find index of the number equals or greater than target from the array
def my_ceil(arr: list, target: int) -> int:
    s = 0
    e = len(arr) - 1

    isAsc = arr[s] < arr[e]

    if(isAsc):
        if(target > arr[e]):
            return -1
    elif(target > arr[s]):
        return -1

    while(s<= e):
        mid = (s+e)//2
        if(arr[mid] == target):
            return mid
        elif(isAsc):
            if(target > arr[mid]):
                s = mid + 1
            else:
                e = mid - 1
        else:
            if(target > arr[mid]):
                e = mid - 1
            else:
                s = mid + 1

    return s
