def missingNumbers(arr):
    aux=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>aux:
            aux=arr[i]
        else:
            return "Error, la cadena de caracteres no esta ordenada"
    minArr=min(arr)
    maxArr=max(arr)
    listArr=[]
    for i in range(minArr,maxArr+1):
        if i not in arr:
            listArr.append(i)
    return listArr
        
print(missingNumbers([1,2,6]))
print(missingNumbers([10,2,6]))
print(missingNumbers([-3,4,8]))
