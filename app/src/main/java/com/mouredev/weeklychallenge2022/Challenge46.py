def robot(arr):
    coord={'x':0,'y':0}    
    for i in range(0,len(arr),2):
        if i%4==0:
            coord['y']+=arr[i]
        else:
            coord['y']-=arr[i]
    for i in range(1,len(arr),2):
        if (i+1)%4==0:
            coord['x']+=arr[i]
        else:
            coord['x']-=arr[i]
    
    return coord



# test
print(robot([10, 5, -2])) # {'x':-5,'y':12}
