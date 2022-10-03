def pascal(n):
    pasc=[]
    if n==1:
        return 1
    if n==2:
        return [1,1]
    for i in range(n):
        if (i==0 or i==n-1):
            num=1
        else:
            anterior=pascal(n-1)
            a=anterior[i]
            b=anterior[i-1]
            num=a+b
        pasc.append(num)
    return pasc
        
print(pascal(1))
print(pascal(2))
print(pascal(3))
print(pascal(4))
print(pascal(5))
print(pascal(6))
print(pascal(7))
print(pascal(8))
print(pascal(9))
print(pascal(10))
