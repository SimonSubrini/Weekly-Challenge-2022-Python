def Armstrong(n):
    if n%1!=0 or n<0:
        return "Ingrese un número entero positivo"
    nTxt=str(n)
    nList=[]
    for num in nTxt:
        nList.append(int(num))
    newN=0
    for i in range(len(nList)):
        newN+=(nList[i]**(len(nList)))
    return newN==n

print(Armstrong(9))    #true
print(Armstrong(407))  #true
print(Armstrong(91))   #false
print(Armstrong(82))   #false
