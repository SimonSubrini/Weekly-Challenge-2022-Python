def WordsCount(txt):
    txtAux=""
    txtDict={}
    for char in txt:
        if char not in ",.{}[]()'¿?":
            txtAux+=char.lower()
    for word in txtAux.split():
        if word in txtDict:
            txtDict[word]+=1
        else:
            txtDict[word]=1
    return txtDict

print(WordsCount("Si Pepe Pecas pica papas con un pico. ¿dónde está el pico con que Pepe Pecas pica papas?"))
