def bum(arr):
    bums=[]
    numBum=0
    for i in range(len(arr)-2):
        if arr[i]==arr[i+2]:
            numBum+=1
            bums.append([arr[i],arr[i+1],arr[i+2]])
    return numBum,bums
 

# test
print(bum([1,2,1])) # 1, prints -> [1,2,1]
print(bum([2, 1, 2, 3, 3, 4, 2, 4])) # 2, prints -> [2, 1, 2] y [4, 2, 4]
