import math

def quickSort(arr):
    if len(arr)==0:
        return []
    indexPivot=math.floor(len(arr)/2)
    pivot=arr[indexPivot]
    leftArr=[]
    rightArr=[]
    result=[]
    for i in range(len(arr)):
        if i!=indexPivot:
            if arr[i]>pivot:
                rightArr.append(arr[i])
            else:
                leftArr.append(arr[i])
    result.extend(quickSort(leftArr))
    result.append(pivot)
    result.extend(quickSort(rightArr))
    print(result)
    return result

  
quickSort([8, 4, -2, 0, 7, 10, 5, -4, -1, 2, 1])
