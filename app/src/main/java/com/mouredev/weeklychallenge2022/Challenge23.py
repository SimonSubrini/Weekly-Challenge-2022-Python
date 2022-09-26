def MCD(n1,n2):
    minNum=min(n1,n2)
    for i in range(minNum+1,2,-1):
        if n1%i==0 and n2%i==0:
            return i
    return 1

def MCM(n1,n2):
    maxNum=max(n1,n2)
    for i in range(maxNum,n1*n2+1):
        if i%n1==0 and i%n2==0:
            return i
    return 1
    

print(MCD(90,45))
print(MCM(9,4))
