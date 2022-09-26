def frame(txt):
    txtList=txt.split()
    longestWord=0
    for word in txtList:
        if len(word)>longestWord:
            longestWord=len(word)
            
    print('*'*(longestWord+4))
    for word in txtList:
        row = '* '+word
        row+=' '*(longestWord+1-len(word))
        row+='*'
        print(row)
    print('*'*(longestWord+4))

frame("¿Qué te parece el reto?")
