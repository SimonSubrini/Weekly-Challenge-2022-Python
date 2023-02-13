def contAq(arr):
    izq=[0,arr[0]]
    Aq=0
    for i in range(1,len(arr)):
        if arr[i]>izq[1] or i==len(arr)-1:
            for j in arr[izq[0]+1:i]:
                Aq+=min(izq[1],arr[i])-j
            izq=[i,arr[i]]
    return Aq



# test
print(contAq([4, 0, 3, 6, 1, 3])) # 7
print(contAq([5, 1, 2, 8, 0, 5])) # 12
