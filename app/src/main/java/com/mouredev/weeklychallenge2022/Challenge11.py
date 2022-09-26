def suprChars(str1:str,str2:str):
    out1=""
    out2=""
    for char in str1:
        if char not in str2:
            out1+=char
    for char in str2:
        if char not in str1:
            out2+=char
    return out1,out2

print(suprChars("Hola","Chau"))
