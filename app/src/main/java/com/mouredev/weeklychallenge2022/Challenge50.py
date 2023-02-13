def karaca(txt):
    res=txt[::-1].lower()
    res=res.replace('a','0')
    res=res.replace('e','1')
    res=res.replace('i','2')
    res=res.replace('o','3')
    res=res.replace('u','4')
    res+='aca'
    return res

#test
print(karaca("hola")) #0l3haca
print(karaca("ChAu")) #40hcaca
print(karaca("Karaca")) #0c0r0kaca
