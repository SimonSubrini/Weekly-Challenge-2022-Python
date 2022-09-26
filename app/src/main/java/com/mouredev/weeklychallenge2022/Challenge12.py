def palindrome(txt):
    txt=norm(txt).lower()
    listTxt=[]
    listTxt2=[]
    for char in txt:
        if char not in " ,.(){}[]¿?¡!":
            listTxt.append(char)
    
    for i in range(len(listTxt)-1,-1,-1):
        listTxt2.append(listTxt[i])
    
    return True if listTxt==listTxt2 else False
            
            
def norm(string):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        string = string.replace(a, b).replace(a.upper(), b.upper())
    return string

print(palindrome("Hola, soy Simón"))
print(palindrome("Ana lleva al oso la avellana"))
