class MountainArray:
    def __init__(self, *arr: int) -> None:
        self.arr = [*arr]

    def get(self, index) -> int:
        return self.arr[index]
    def length(self) -> int:
        return len(self.arr)

    def peakElementIndex(self, mountain_arr):
            s = 0
            e = mountain_arr.length() - 1
            while(s < e):
                mid = (s + e)//2
                if(mountain_arr.get(mid + 1) > mountain_arr.get(mid)):
                    s = mid + 1
                else:
                    e = mid
            return e

    def binarySearch(self, arr: list, toFind: int, s, e):
        while(s <= e):
            mid = (s + e)//2
            if(arr.get(mid) == toFind):
                return mid
            elif(toFind > arr.get(mid)):
                s = mid + 1
            else:
                e = mid - 1
        return -1
    
    def binarySearchDesc(self, arr: list, toFind: int, s, e):
        while(s <= e):
            mid = (s + e)//2
            if(arr.get(mid) == toFind):
                return mid
            elif(toFind > arr.get(mid)):
                e = mid - 1
            else:
                s = mid + 1
        return -1

    def findInMountainArray(self, target: int, mountain_arr) -> int:
        peakIndex = self.peakElementIndex(mountain_arr)
        print(peakIndex)
        if(mountain_arr.get(peakIndex) == target):
            return peakIndex
        else:
            index = self.binarySearch(mountain_arr, target, 0, peakIndex-1)
            if(index != -1):
                return index
            else:
                return self.binarySearchDesc(mountain_arr, target, peakIndex+1, mountain_arr.length()-1)


lis = MountainArray(0,5,3,1)
print(lis.findInMountainArray(1,lis))