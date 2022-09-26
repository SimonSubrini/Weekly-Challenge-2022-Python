def conj(arr1,arr2,cond):
    result=[]
    if cond:
        for element in arr1:
            if element in arr2 and element not in result:
                result.append(element)
    else:
        for element in arr1:
            if element not in arr2 and element not in result:
                result.append(element)
        for element in arr2:
            if element not in arr1 and element not in result:
                result.append(element)
    return result

print(conj([1,2,3,4,5,6],[4,5,6,7,8,9],True))
print(conj([1,2,3,4,5,6],[4,5,6,7,8,9],False))
