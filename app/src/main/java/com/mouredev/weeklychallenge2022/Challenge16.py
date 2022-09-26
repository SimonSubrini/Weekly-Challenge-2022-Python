def Mayus(txt:str):
    newTxt=''
    for word in txt.split():
        newWord=word[0].upper()
        newWord+=word[1:]
        newTxt+=newWord+' '
    return newTxt
        
print(Mayus("Hola mi nombre es simon"))
