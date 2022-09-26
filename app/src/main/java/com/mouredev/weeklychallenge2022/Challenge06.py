def invString(txt):
    revTxt=""
    revList=[]
    for char in txt:
        revList.append(char)
    n=len(revList)
    for i in range(n):
        revTxt+=revList[n-i-1]
    return revTxt
    
print(invString("Hola mundo"))
