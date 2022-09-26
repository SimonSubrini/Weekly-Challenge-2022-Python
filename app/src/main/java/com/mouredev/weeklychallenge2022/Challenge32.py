def second(arr):
    arrAux=[float('-inf'),float('-inf')]
    for i in range(len(arr)):
        if arr[i]>arrAux[0]:
            arrAux[1]=arrAux[0]
            arrAux[0]=arr[i]
    return arrAux[1]
print(second([1,5,6,4,2,1,0,8]))
print(second([1,2,4,0,3,0,4,10]))
print(second([0.04,0.1,-4,-0.83]))
