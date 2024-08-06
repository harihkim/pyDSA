#https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

def findIt(arr: list, target: str) -> str:
    s = 0
    e = len(arr) - 1

    if(target > arr[e]):
        return arr[0]

    while(s<=e):

        mid = (s+e)//2
        if(target < arr[mid]):
            e = mid - 1
        else:
            s = mid + 1
        
    return arr[s]
