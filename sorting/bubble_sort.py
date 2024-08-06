
#inplace
def bubble_sort(arr: list):
    size = len(arr)

    for i in range(size):
        swaped = False
        for j in range(size-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1], arr[j]
                swaped=True
        if(not swaped):
           break
        else:
            swaped = False

myArr = [8,5,7,3,6]
bubble_sort(myArr)
print(myArr)